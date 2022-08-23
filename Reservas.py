from tkinter import	*
from tkinter import ttk
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

def reservas_tabela():

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

    titulo_r = Label(janela_r, text='Reservas cadastradas', font=dsn['fonte1'], fg=dsn['laranja1'])
    cadastar_r = Button(janela_r, text='Reservar', fg=dsn['branco'] ,bg=dsn['laranja1'],relief=dsn['relif'], font=dsn['fonte4'],)

    titulo_r.grid(columnspan=5, column=1, rowspan=3, row=0, )
    y = 310
    cadastar_r.place(x=340, y=y)

    janela_r.mainloop()

if __name__=='__main__':
    reservas_tabela()