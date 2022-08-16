from tkinter import	*
from tkinter import ttk
from tkinter import messagebox
import sqlite3

banco = sqlite3.connect('Central-Ferramentas.db')
cursor = banco.cursor()

#conectando com a tabela do banco de dados
tabela = 'técnicos'
elementos = 'Nome,Contato,Email,Turno,Equipe,Id'
cursor.execute(f"SELECT {elementos} FROM {tabela} " )

#pegando valores
colunas_nomes= [nome[0] for nome in cursor.description]
valores = cursor.fetchall()

#criando janela e treeview
janela = Tk()
tecnicos = ttk.Treeview(janela)
tecnicos['columns'] = colunas_nomes
tecnicos.column('#0', width=40,anchor=W)#coluna de index

#barra de rolagem
vsb = ttk.Scrollbar(janela, orient="vertical", command=tecnicos.yview)
vsb.pack(side='right', fill='y')
tecnicos.configure(yscrollcommand=vsb.set)

# criando colunas
for nome in colunas_nomes:
    tecnicos.column(nome, anchor=CENTER,width=150)
    tecnicos.heading(nome,text=nome)

# inserindo varlores
ids = range(len(valores))
for v,i in zip(valores,ids):
    tecnicos.insert('','end', text=i, values=v)


def excluir():
    selecionar = tecnicos.selection()[0]
    selecionado = tecnicos.item(selecionar,'values')
    msg = messagebox.askquestion('deletar', f"Deletar {selecionado[0].upper()}, ID: {selecionado[-1]} ? ")
    if msg == 'yes':
        cursor.execute(f"DELETE from técnicos WHERE Id='{selecionado[-1]}' ")
        tecnicos.delete(selecionar)
        banco.commit()


excluir_t = Button(janela,text='excluir',command=excluir)

tecnicos.pack()
excluir_t.pack()

janela.mainloop()