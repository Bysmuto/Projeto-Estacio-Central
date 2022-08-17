from tkinter import	*
from tkinter import ttk
from tkinter import messagebox
from Cadastrar_Ferramentas import casdastro_ferramenta
from exportar import exportar
import sqlite3

def ferramentas():

    janela_f = Tk()

    #centralizando a tela
    janela_altura = 400
    janela_largura = 1000
    tela_larg = janela_f.winfo_screenwidth()
    tela_alt = janela_f.winfo_screenheight()
    x = int((tela_larg / 2) - (janela_largura / 2))
    y = int((tela_alt / 2) - (janela_altura / 2))
    janela_f.geometry(f"{janela_largura}x{janela_altura}+{x}+{y}")
    janela_f.resizable(False, False)

    #Banco de dados:
    banco = sqlite3.connect('Central-Ferramentas.db')
    cursor = banco.cursor()

    # itens da tabela do banco
    tabela = 'ferramentas'
    elementos = '*'
    cursor.execute(f"SELECT {elementos} FROM {tabela} ")
    colunas_nomes = [nome[0] for nome in cursor.description]
    valores = cursor.fetchall()

    #Tabela do Tk
    ferramentas = ttk.Treeview(janela_f, selectmode='browse')
    ferramentas['columns'] = colunas_nomes
    ferramentas.column('#0', width=40)# coluna de index

    #barra de rolagem
    vsb = ttk.Scrollbar(janela_f, orient="vertical", command=ferramentas.yview)
    vsb.pack(side='right', fill='y')
    ferramentas.configure(yscrollcommand=vsb.set)

    # inserindo valores na Tabela do tk
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
                janela_f.destroy()

        except IndexError:
            erro = messagebox.showinfo('Erro','Selecione um item')

    def modificar():
        try:
            def janela2():

                selecionar = ferramentas.selection()[0]
                selecionado = ferramentas.item(selecionar, 'values')
                print(selecionado)
                dsn = {'fonte1': 'Arial 20',
                          'fonte2': 'Arial 14',
                          'laranja1': '#F76A57',
                          'preto': '#2e2e2d',
                          'laranja2': '#F4D9D7',
                          'relif': FLAT,
                          'y_dist': 5,
                          'x_dist': 10, }

                janela2 = Tk()

                titulo = Label(janela2, text=' Modificar Ferramenta', font=dsn['fonte1'], fg=dsn['laranja1'])
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
                    nome = Label(janela2, text=n, font=dsn['fonte2'], fg=dsn['preto'], )
                    nome.grid(column=0, row=c, sticky=W, pady=dsn['y_dist'], padx=dsn['x_dist'])

                entrada_descricao = Entry(janela2, font=dsn['fonte2'], fg=dsn['preto'], relief=dsn['relif'], bg=dsn['laranja2'])
                entrada_descricao.insert(0,selecionado[0])

                entrada_Fabricante = Entry(janela2, font=dsn['fonte2'], fg=dsn['preto'], relief=dsn['relif'], bg=dsn['laranja2'])

                entrada_Voltagem = Entry(janela2, font=dsn['fonte2'], fg=dsn['preto'], relief=dsn['relif'], bg=dsn['laranja2'])

                entrada_Number = Entry(janela2, font=dsn['fonte2'], fg=dsn['preto'], relief=dsn['relif'], bg=dsn['laranja2'])

                entrada_Tamanho = Entry(janela2, font=dsn['fonte2'], fg=dsn['preto'], relief=dsn['relif'],bg=dsn['laranja2'])

                entrada_medida = Entry(janela2, font=dsn['fonte2'], fg=dsn['preto'], relief=dsn['relif'],bg=dsn['laranja2'])

                entrada_Material = Entry(janela2, font=dsn['fonte2'], fg=dsn['preto'], relief=dsn['relif'],bg=dsn['laranja2'])

                entrada_tipo = Entry(janela2, font=dsn['fonte2'], fg=dsn['preto'], relief=dsn['relif'],bg=dsn['laranja2'])

                entradas_f = (entrada_descricao,
                              entrada_Fabricante,
                              entrada_Voltagem,
                              entrada_Number,
                              entrada_Tamanho,
                              entrada_medida,
                              entrada_Material,
                              entrada_tipo,)

                for e,i in zip(entradas_f,selecionado):
                    e.insert(0,i)

                for e, c in zip(entradas_f, cords_y):
                    e.grid(column=1, row=c, padx=dsn['x_dist'], pady=dsn['y_dist'])

                def enviar():

                    banco = sqlite3.connect('Central-Ferramentas.db')
                    cursor = banco.cursor()

                    pegar_entradas = [ent.get() for ent in entradas_f]
                    print(pegar_entradas)

                    for cn,pe in zip(colunas_nomes,pegar_entradas):
                        cursor.execute(f"UPDATE ferramentas SET {cn}=?  WHERE Id='{selecionado[-1]}'",(pe,))
                    banco.commit()
                    banco.close()
                    janela2.destroy()
                    print(f'Ferramenta {selecionado[-1]} modificada')

                cadastrar = Button(janela2, text='Enviar', command=enviar, font=dsn['fonte2'], fg=dsn['laranja1'], relief=dsn['relif'])
                cadastrar.grid(column=0, row=len(nomes) + 1, columnspan=2, pady=dsn['y_dist'])

                janela_f.mainloop()
            janela2()

        except IndexError:
            erro = messagebox.showinfo('Erro', 'Selecione um item')

    cadastar_f = Button(janela_f, text='Nova Ferramenta', command=casdastro_ferramenta)
    excluir_f = Button(janela_f, text='Excluir', command=excluir)
    modificar_f = Button(janela_f, text='Modificar', command=modificar)
    exportar_f =Button(janela_f, text='Exportar', command=exportar)

    ferramentas.pack()
    cadastar_f.pack()
    excluir_f.pack()
    modificar_f.pack()
    exportar_f.pack()

    janela_f.mainloop()

if __name__=='__main__':
    ferramentas()