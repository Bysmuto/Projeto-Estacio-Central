from tkinter import	*
from tkinter import ttk
import sqlite3

banco = sqlite3.connect('Central-Ferramentas.db')
cursor = banco.cursor()

tabela = 'técnicos'
elementos = 'Nome,Contato,Email,Turno,Equipe'
cursor.execute(f"SELECT {elementos} FROM {tabela} " )
colunas_nomes= [nome[0] for nome in cursor.description]
valores = cursor.fetchall()

janela = Tk()
tecnicos = ttk.Treeview(janela)
tecnicos['columns'] = colunas_nomes
tecnicos.column('#0', width=40,anchor=W)

vsb = ttk.Scrollbar(janela, orient="vertical", command=tecnicos.yview)
vsb.pack(side='right', fill='y')
tecnicos.configure(yscrollcommand=vsb.set)

# criando colunas
for nome in colunas_nomes:
    tecnicos.column(nome, anchor=CENTER,width=150)
    tecnicos.heading(nome,text=nome)

# inserindo varlores

ids = range(len(valores))
print(ids)
for v,i in zip(valores,ids):
    tecnicos.insert('','end', text=i, values=v)

tecnicos.pack()






janela.mainloop()