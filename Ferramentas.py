from tkinter import	*
from tkinter import ttk
from tkinter import messagebox
from Cadastrar_Ferramentas import casdastro_ferramenta
from exportar_f import exportar_f
import sqlite3
dsn = {   'fonte1': 'Franklin 25 bold',
          'fonte4': 'Franklin 14 bold',
          'fonte2': 'Yu 15',
          'fonte3': 'Arial 12',
          'laranja1': '#F76A57',
          'preto': '#2e2e2d',
          'branco':'#fafafa',
          'branco2': 'white',
          'laranja2': '#F4D9D7',
          'relif': FLAT,
          'y_dist': 10,
          'x_dist': 20,         }

def ferramentas():

    janela_f = Tk()
    janela_f.configure()
    estilo = ttk.Style()
    estilo.configure("Treeview.Heading", font=(dsn['fonte2'], 13, 'bold'), foreground=dsn['laranja1'],)
    estilo.configure("Treeview", highlightthickness=100, bd=100, font=('Calibri', 12,))
    estilo.map('Treeview', background=[(' selected', dsn['laranja1'])])

    #centralizando a tela
    janela_altura = 400
    janela_largura = 1000
    tela_larg = janela_f.winfo_screenwidth()
    tela_alt = janela_f.winfo_screenheight()
    x = int((tela_larg / 2) - (janela_largura / 2))
    y = int((tela_alt / 2.5) - (janela_altura / 2))
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


    ferramentas = ttk.Treeview(janela_f, selectmode='browse',)
    ferramentas['columns'] = colunas_nomes
    ferramentas.column('#0', width=40)# coluna de index

    #barra de rolagem
    rolagem = ttk.Scrollbar(janela_f, orient="vertical", command=ferramentas.yview)
    ferramentas.configure(yscrollcommand=rolagem.set)

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


    titulo_f = Label(janela_f,text='Ferramentas cadastradas',font=dsn['fonte1'],fg=dsn['laranja1'])
    cadastar_f = Button(janela_f, text='Nova Ferramenta', command=casdastro_ferramenta,bg=dsn['laranja1'],relief=dsn['relif'],font=dsn['fonte4'],fg=dsn['branco2'])
    excluir_f = Button(janela_f, text='Excluir', command=excluir,bg=dsn['laranja1'],relief=dsn['relif'],font=dsn['fonte4'],fg=dsn['branco2'])
    modificar_f = Button(janela_f, text='Modificar', command=modificar,bg=dsn['laranja1'],relief=dsn['relif'],font=dsn['fonte4'],fg=dsn['branco2'])
    exportar_f_ =Button(janela_f, text='Exportar', command=exportar_f,bg=dsn['laranja1'],relief=dsn['relif'],font=dsn['fonte4'],fg=dsn['branco2'])


    #posicionamento
    titulo_f.grid(columnspan=5,column=1,rowspan=3,row=0,)
    ferramentas.grid(columnspan=5,column=1,rowspan=3,row=3,padx=20,pady=20)
    rolagem.place(in_=ferramentas,relx=1,rely=0,relheight=1)


    y = 310
    cadastar_f.place(x=165,y=y)
    modificar_f.place(x=385,y=y)
    excluir_f.place(x=535,y=y)
    exportar_f_.place(x=665,y=y)

    janela_f.mainloop()

if __name__=='__main__':
    ferramentas()