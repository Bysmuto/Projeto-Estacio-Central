from tkinter import	*
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def ferramentas():
    banco = sqlite3.connect('Central-Ferramentas.db')
    cursor = banco.cursor()

    tabela = 'ferramentas'
    elementos = '*'
    cursor.execute(f"SELECT {elementos} FROM {tabela} " )

    colunas_nomes= [nome[0] for nome in cursor.description]
    valores = cursor.fetchall()

    janela = Tk()

    ferramentas = ttk.Treeview(janela, selectmode='browse')

    vsb = ttk.Scrollbar(janela, orient="vertical", command=ferramentas.yview)
    vsb.pack(side='right', fill='y')
    ferramentas.configure(yscrollcommand=vsb.set)


    ferramentas['columns'] = colunas_nomes

    ferramentas.column('#0', width=40)# coluna de index

    # inserindo varlores
    for nome in colunas_nomes:
        ferramentas.column(nome, width=100, anchor=CENTER)
        ferramentas.heading(nome, text=nome)

    ids = range(len(valores))
    for v,i in zip(valores,ids):#numero das linhas
        ferramentas.insert('', 'end', text=i, values=v)

    #funcionalidades

    def excluir():
        try:
            selecionar = ferramentas.selection()[0]
            selecionado = ferramentas.item(selecionar,'values')
            msg = messagebox.askquestion('deletar', f"Deletar {selecionado[0].upper()}, ID: {selecionado[-1]} ? ")
            if msg == 'yes':
                cursor.execute(f"DELETE from ferramentas WHERE Id='{selecionado[-1]}' ")
                ferramentas.delete(selecionar)
                banco.commit()
        except IndexError:
            erro = messagebox.showinfo('Erro','Selecione um item')

    def modificar():

        try:

            selecionar = ferramentas.selection()[0]
            selecionado = ferramentas.item(selecionar, 'values')

            def janela2():
                design = {'fonte1': 'Arial 20',
                          'fonte2': 'Arial 14',
                          'laranja1': '#F76A57',
                          'preto': '#2e2e2d',
                          'laranja2': '#F4D9D7',
                          'relif': FLAT,
                          'y_dist': 5,
                          'x_dist': 10, }

                janela = Tk()

                titulo = Label(janela, text='Modificar Ferramenta', font=design['fonte1'], fg=design['laranja1'])
                titulo.grid(column=0, row=0, columnspan=2, pady=10)

                nomes = ('Descrição:',
                         'Fabricante :',
                         'Voltagem :',
                         'Part Number :',
                         'Tamanho :',
                         'Medida :',
                         'Material :',
                         'Tipo :',)

                cords_y = (range(1, len(nomes) + 1))

                for n, c in zip(nomes, cords_y):
                    nome = Label(janela, text=n, font=design['fonte2'], fg=design['preto'], )
                    nome.grid(column=0, row=c, sticky=W, pady=design['y_dist'], padx=design['x_dist'])

                entrada_descricao = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'],
                                          bg=design['laranja2'])
                entrada_id = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'],
                                   bg=design['laranja2'])
                entrada_Fabricante = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'],
                                           bg=design['laranja2'])
                entrada_Voltagem = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'],
                                         bg=design['laranja2'])
                entrada_Number = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'],
                                       bg=design['laranja2'])
                entrada_Tamanho = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'],
                                        bg=design['laranja2'])
                entrada_medida = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'],
                                       bg=design['laranja2'])
                entrada_Material = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'],
                                         bg=design['laranja2'])
                entrada_tipo = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'],
                                     bg=design['laranja2'])

                entradas_f = (entrada_descricao,
                              entrada_Fabricante,
                              entrada_Voltagem,
                              entrada_Number,
                              entrada_Tamanho,
                              entrada_medida,
                              entrada_Material,
                              entrada_tipo,)

                for e, c in zip(entradas_f, cords_y):
                    e.grid(column=1, row=c, padx=design['x_dist'], pady=design['y_dist'])

                def enviar():

                    banco = sqlite3.connect('Central-Ferramentas.db')
                    cursor = banco.cursor()

                    pegar_entradas = [ent.get() for ent in entradas_f]
                    print(pegar_entradas)

                    for cn,pe in zip(colunas_nomes,pegar_entradas):
                        cursor.execute(f"UPDATE ferramentas SET {cn}=?  WHERE Id='{selecionado[-1]}'",(pe,))
                    banco.commit()
                    banco.close()
                    janela.destroy()
                    print(f'Ferramenta {selecionado[-1]} modificada')

                cadastrar = Button(janela, text='Enviar', command=enviar, font=design['fonte2'], fg=design['laranja1'],relief=design['relif'])
                cadastrar.grid(column=0, row=len(nomes) + 1, columnspan=2, pady=design['y_dist'])


                janela.mainloop()

            janela2()

        except IndexError:
            erro = messagebox.showinfo('Erro', 'Selecione um item')


    excluir_f = Button(janela,text='Excluir',command=excluir)
    modificar_f = Button(janela, text='Modificar', command=modificar)

    ferramentas.pack()
    excluir_f.pack()
    modificar_f.pack()
    janela.mainloop()

if __name__=='__main__':
    ferramentas()