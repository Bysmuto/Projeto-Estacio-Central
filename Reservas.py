from tkinter import	*
from tkinter import ttk
import sqlite3
from centralizar import centralizar
from exportar_f import exportar_f

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


def reservas_tabela():

    global tabela
    janela_r = Tk()
    janela_r.title('Reservas')
    estilo = ttk.Style()
    estilo.configure("Treeview.Heading", font=(dsn['fonte2'], 13, 'bold'), foreground=dsn['laranja1'],)
    estilo.configure("Treeview", highlightthickness=100, bd=100, font=('Calibri', 12,))
    estilo.map('Treeview', background=[(' selected', dsn['laranja1'])])

    centralizar(janela_r,400,800)

    def tabela():
        global ferramentas_tabela, cursor, banco, colunas_nomes, valores
        # Banco de dados:
        banco = sqlite3.connect('Central-Ferramentas.db')
        cursor = banco.cursor()

        # itens da tabela do banco
        tabela = 'Reservas'
        elementos = '*'
        cursor.execute(f"SELECT {elementos} FROM {tabela} ")
        colunas_nomes = [nome[0] for nome in cursor.description]
        valores = cursor.fetchall()

        # Tabela do Tk
        ferramentas_tabela = ttk.Treeview(janela_r, selectmode='browse', )
        ferramentas_tabela['columns'] = colunas_nomes
        ferramentas_tabela.column('#0', width=40)  # coluna de index

        # barra de rolagem
        rolagem = ttk.Scrollbar(janela_r, orient="vertical", command=ferramentas_tabela.yview)
        ferramentas_tabela.configure(yscrollcommand=rolagem.set)

        # inserindo valores na Tabela do tk
        for nome in colunas_nomes:
            ferramentas_tabela.column(nome, width=100, anchor=CENTER)
            ferramentas_tabela.heading(nome, text=nome)

        ids = range(len(valores))
        for v, i in zip(valores, ids):  # numero das linhas
            ferramentas_tabela.insert('', 'end', text=i, values=v)

        ferramentas_tabela.grid(columnspan=1, column=1, rowspan=3, row=3, padx=20, pady=20)
        rolagem.place(in_=ferramentas_tabela, relx=1, rely=0, relheight=1)
    tabela()

    titulo_r   = Label(janela_r, text='Reservas cadastradas', font=dsn['fonte1'], fg=dsn['laranja1'])
    cadastar_r = Button(janela_r, text='Reservar',command=casdastro_reserva ,fg=dsn['branco'] ,bg=dsn['laranja1'],relief=dsn['relif'], font=dsn['fonte4'],)
    exportar_r = Button(janela_r, text='Exportar', command=lambda :exportar_f('Reservas','Reserva da Central'),bg=dsn['laranja1'],relief=dsn['relif'],font=dsn['fonte4'],fg=dsn['branco2'])
    excluir_r  =  Button(janela_r, text='Excluir',command=excluir ,fg=dsn['branco'] ,bg=dsn['laranja1'],relief=dsn['relif'], font=dsn['fonte4'],)

    titulo_r.grid(columnspan=5, column=1, rowspan=3, row=0, )
    y = 310
    cadastar_r.place(x=340, y=y)
    exportar_r.place(x=540, y=y)
    excluir_r.place(x=160, y=y)


    janela_r.mainloop()

#funcionalidades

def casdastro_reserva():

    design = {'fonte1': 'Arial 25',
              'fonte2': 'Arial 15',
              'laranja1': '#F76A57',
              'preto': '#2e2e2d',
              'laranja2' : '#F4D9D7',
              'relif': FLAT,
              'y_dist':5,
               'x_dist':10,}

    janela = Tk()

    centralizar(janela,400,400)

    titulo = Label(janela, text='Cadastrar Reserva', font=design['fonte1'], fg=design['laranja1'])
    titulo.grid(column=0, row=0, columnspan=2, pady=10,padx=10)

    nomes = ('Ferramenta:',
             'Id F :',
             'Técnico :',
             'Id T :',
             'Tempo :',
             'Inicio :',
             'Entrega :',
             )

    cords_y =(range(1, len(nomes) + 1))

    for n, c in zip(nomes, cords_y):
        nome = Label(janela, text=n, font=design['fonte2'], fg=design['preto'],)
        nome.grid(column=0, row=c,sticky=W,pady=design['y_dist'],padx=design['x_dist'])


    Ferramenta  = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'], bg=design['laranja2'])
    IdF         = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'], bg=design['laranja2'])
    Tecnico     = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'], bg=design['laranja2'])
    IdT         = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'],bg=design['laranja2'])
    tempo       = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'], bg=design['laranja2'])
    inicio      = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'], bg=design['laranja2'])
    entrega     = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'], bg=design['laranja2'])

    entradas_f = (Ferramenta,
                  IdF,
                  Tecnico,
                  IdT,
                  tempo,
                  inicio,
                  entrega,
                  )


    for e, c in zip(entradas_f, cords_y):
        e.grid(column=1, row=c,padx=design['x_dist'],pady=design['y_dist'])

    def cadastro():
        banco = sqlite3.connect('Central-Ferramentas.db')
        cursor = banco.cursor()

        pegar_entradas = [ent.get() for ent in entradas_f]
        print(pegar_entradas)

        quant_valores = '?,' * (len(entradas_f)-1) + '?'
        print(quant_valores)
        cursor.execute(f"INSERT OR IGNORE INTO Reservas VALUES({quant_valores})", (pegar_entradas))

        banco.commit()
        banco.close()
        print(f'Reserva {Ferramenta.get()} reservada')
        janela.destroy()


        # update na tabela
        ferramentas_tabela.destroy()
        tabela()


    cadastrar = Button(janela, text='Enviar', command=cadastro, font=design['fonte2'], fg=design['laranja1'],
                       relief=design['relif'])

    cadastrar.grid(column=0, row=len(nomes)+1, columnspan=2, pady=design['y_dist'])

    janela.mainloop()

def excluir():
        try:
            selecionar = ferramentas_tabela.selection()[0]
            print(selecionar)
            selecionado = ferramentas_tabela.item(selecionar, 'values')
            print(selecionado)
            cursor.execute(f"DELETE from Reservas WHERE IdF='{selecionado[1]}' ")
            ferramentas_tabela.delete(selecionar)
            banco.commit()
        except IndexError:
            print('Erro','Selecione um item')

if __name__=='__main__':
    reservas_tabela()