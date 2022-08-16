from tkinter import	*
from tkinter import ttk
import sqlite3

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

# criando colunas
for nome in colunas_nomes:
    ferramentas.column(nome, width=100, anchor=CENTER)
    ferramentas.heading(nome, text=nome)

# inserindo varlores

ids = range(len(valores))
for v,i in zip(valores,ids):
    ferramentas.insert('', 'end', text=i, values=v)
ferramentas.pack()

janela.mainloop()