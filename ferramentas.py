from tkinter import	*
from tkinter import ttk
from tkinter import messagebox
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


excluir_f = Button(janela,text='excluir',command=excluir)


ferramentas.pack()
excluir_f.pack()
janela.mainloop()