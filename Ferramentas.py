from tkinter import	*
from tkinter import ttk
from Cadastrar_Ferramentas import casdastro_ferramenta
from exportar_f import exportar_f
import sqlite3
from centralizar import centralizar

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

def ferramentas_tabela():

    janela_f = Tk()
    janela_f.title('Ferramentas')
    estilo = ttk.Style()
    estilo.configure("Treeview.Heading", font=(dsn['fonte2'], 13, 'bold'), foreground=dsn['laranja1'],)
    estilo.configure("Treeview", highlightthickness=100, bd=100, font=('Calibri', 12,))
    estilo.map('Treeview', background=[(' selected', dsn['laranja1'])])

    centralizar(janela_f,400,1000)

    def tabela():
        global ferramentas_tabela,cursor,banco,colunas_nomes,valores
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
        ferramentas_tabela = ttk.Treeview(janela_f, selectmode='browse', )
        ferramentas_tabela['columns'] = colunas_nomes
        ferramentas_tabela.column('#0', width=40)# coluna de index

        #barra de rolagem
        rolagem = ttk.Scrollbar(janela_f, orient="vertical", command=ferramentas_tabela.yview)
        ferramentas_tabela.configure(yscrollcommand=rolagem.set)

        # inserindo valores na Tabela do tk
        for nome in colunas_nomes:
            ferramentas_tabela.column(nome, width=100, anchor=CENTER)
            ferramentas_tabela.heading(nome, text=nome)

        ids = range(len(valores))
        for v,i in zip(valores,ids):#numero das linhas
            ferramentas_tabela.insert('', 'end', text=i, values=v)

        ferramentas_tabela.grid(columnspan=5, column=1, rowspan=3, row=3, padx=20, pady=20)
        rolagem.place(in_=ferramentas_tabela, relx=1, rely=0, relheight=1)
    tabela()

    #funcionalidades

    def casdastro_ferramenta():

        design = {'fonte1': 'Arial 20',
                  'fonte2': 'Arial 14',
                  'laranja1': '#F76A57',
                  'preto': '#2e2e2d',
                  'laranja2': '#F4D9D7',
                  'relif': FLAT,
                  'y_dist': 5,
                  'x_dist': 10, }

        janela = Tk()

        # centralizando a tela
        janela_altura = 410
        janela_largura = 400
        tela_larg = janela.winfo_screenwidth()
        tela_alt = janela.winfo_screenheight()
        x = int((tela_larg / 2.8) - (janela_largura / 2))
        y = int((tela_alt / 2) - (janela_altura / 2))
        janela.geometry(f"{janela_largura}x{janela_altura}+{x}+{y}")
        janela.configure()
        janela.resizable(False, False)

        titulo = Label(janela, text='Cadastrar Ferramenta', font=design['fonte1'], fg=design['laranja1'])
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

        def cadastro():
            banco = sqlite3.connect('Central-Ferramentas.db')
            cursor = banco.cursor()

            pegar_entradas = [ent.get() for ent in entradas_f] + [None]

            quant_valores = '?,' * len(entradas_f) + '?'
            cursor.execute(f"INSERT OR IGNORE INTO ferramentas VALUES({quant_valores})", (pegar_entradas))

            banco.commit()
            banco.close()
            print(f'Ferramenta {entrada_descricao.get()} cadastrada')
            janela.destroy()

            # update na tabela
            ferramentas_tabela.destroy()
            tabela()

        cadastrar = Button(janela, text='Enviar', command=cadastro, font=design['fonte2'], fg=design['laranja1'],
                           relief=design['relif'])

        cadastrar.grid(column=0, row=len(nomes) + 1, columnspan=2, pady=design['y_dist'])

        janela.mainloop()

    def excluir():
        try:
            selecionar = ferramentas_tabela.selection()[0]
            selecionado = ferramentas_tabela.item(selecionar, 'values')
            cursor.execute(f"DELETE from ferramentas WHERE Id='{selecionado[-1]}' ")
            ferramentas_tabela.delete(selecionar)
            banco.commit()


        except IndexError:
            erro = messagebox.showinfo('Erro','Selecione um item')

    def modificar():
        try:
            def janela2():

                selecionar = ferramentas_tabela.selection()[0]
                selecionado = ferramentas_tabela.item(selecionar, 'values')
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

                    #update na tabela
                    ferramentas_tabela.destroy()
                    tabela()

                    print(f'Ferramenta {selecionado[-1]} modificada')

                cadastrar = Button(janela2, text='Enviar', command=enviar, font=dsn['fonte2'], fg=dsn['laranja1'], relief=dsn['relif'])
                cadastrar.grid(column=0, row=len(nomes) + 1, columnspan=2, pady=dsn['y_dist'])

                janela_f.mainloop()
            janela2()

        except IndexError:
            print('Erro', 'Selecione um item')


    titulo_f = Label(janela_f,text='Ferramentas cadastradas',font=dsn['fonte1'],fg=dsn['laranja1'])
    cadastar_f = Button(janela_f, text='Nova Ferramenta', command=casdastro_ferramenta,bg=dsn['laranja1'],relief=dsn['relif'],font=dsn['fonte4'],fg=dsn['branco2'])
    excluir_f = Button(janela_f, text='Excluir', command=excluir,bg=dsn['laranja1'],relief=dsn['relif'],font=dsn['fonte4'],fg=dsn['branco2'])
    modificar_f = Button(janela_f, text='Modificar', command=modificar,bg=dsn['laranja1'],relief=dsn['relif'],font=dsn['fonte4'],fg=dsn['branco2'])
    exportar_f_ =Button(janela_f, text='Exportar', command=lambda :exportar_f('ferramentas','Ferramentas da Central'),bg=dsn['laranja1'],relief=dsn['relif'],font=dsn['fonte4'],fg=dsn['branco2'])


    #posicionamento
    titulo_f.grid(columnspan=5,column=1,rowspan=3,row=0,)

    y = 310
    cadastar_f.place(x=165,y=y)
    modificar_f.place(x=385,y=y)
    excluir_f.place(x=535,y=y)
    exportar_f_.place(x=665,y=y)

    janela_f.mainloop()

if __name__=='__main__':
    ferramentas_tabela()