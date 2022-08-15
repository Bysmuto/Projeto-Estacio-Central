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
tecnicos = ttk.Treeview(janela)
tecnicos['columns'] = colunas_nomes
tecnicos.column('#0', width=1)

# criando colunas
for nome in colunas_nomes:
    tecnicos.column(nome, width=100)
    tecnicos.heading(nome,text=nome)

# inserindo varlores
for v in valores:
    tecnicos.insert('','end', text='', values=v)

tecnicos.pack()






janela.mainloop()