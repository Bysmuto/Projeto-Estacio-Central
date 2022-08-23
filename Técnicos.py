from tkinter import	*
from tkinter import ttk
from tkinter import messagebox
from exportar_t import exportar_t
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


def tecnicos():
    banco = sqlite3.connect('Central-Ferramentas.db')
    cursor = banco.cursor()

    #conectando com a tabela do banco de dados
    tabela = 'técnicos'
    elementos = 'Nome,Contato,Email,Turno,Equipe,Id'
    cursor.execute(f"SELECT {elementos} FROM {tabela} " )

    #pegando valores
    colunas_nomes= [nome[0] for nome in cursor.description]#retorna o nome de cada coluna
    valores = cursor.fetchall()

    #criando janela e treeview
    janela = Tk()
    janela.title('Técnicos')

    # centralizando a tela
    janela_altura = 400
    janela_largura = 1000
    tela_larg = janela.winfo_screenwidth()
    tela_alt = janela.winfo_screenheight()
    x = int((tela_larg / 2) - (janela_largura / 2))
    y = int((tela_alt / 2.5) - (janela_altura / 2))
    janela.geometry(f"{janela_largura}x{janela_altura}+{x}+{y}")
    janela.resizable(False, False)

    tecnicos = ttk.Treeview(janela)
    tecnicos['columns'] = colunas_nomes
    tecnicos.column('#0', width=40,anchor=W)#coluna de index

    #barra de rolagem
    rolagem = ttk.Scrollbar(janela, orient="vertical", command=tecnicos.yview)
    tecnicos.configure(yscrollcommand=rolagem.set)

    # inserindo varlores nas colunas

    for nome in colunas_nomes:
        tecnicos.column(nome, anchor=CENTER,width=150)
        tecnicos.heading(nome,text=nome)

    ids = range(len(valores))
    for v,i in zip(valores,ids): #numero da linha
        tecnicos.insert('','end', text=i, values=v)

    #funcionalidades

    # def excluir():
    #     try:
    #         selecionar = tecnicos.selection()[0]
    #         selecionado = tecnicos.item(selecionar,'values')
    #         msg = messagebox.askquestion('deletar', f"Deletar {selecionado[0].upper()}, ID: {selecionado[-1]} ? ")
    #         if msg == 'yes':
    #             cursor.execute(f"DELETE from técnicos WHERE Id='{selecionado[-1]}' ")
    #             tecnicos.delete(selecionar)
    #             banco.commit()
    #     except IndexError:
    #         erro = messagebox.showinfo('Erro','Selecione um item')

    titulo_t = Label(janela,text='Técnicos cadastradas',font=dsn['fonte1'],fg=dsn['laranja1'])
    exportar_t_= Button(janela, text='Exportar', command=exportar_t,bg=dsn['laranja1'],relief=dsn['relif'],font=dsn['fonte4'],fg=dsn['branco2'])

    #posicionamento
    y = 310
    rolagem.place(in_=tecnicos, relx=1, rely=0, relheight=1)
    titulo_t.grid(columnspan=5, column=1, rowspan=3, row=0, )
    tecnicos.grid(columnspan=5,column=1,rowspan=3,row=3,padx=20,pady=20)
    exportar_t_.place(x=450,y=y)
    janela.mainloop()

if __name__=='__main__':
    tecnicos()