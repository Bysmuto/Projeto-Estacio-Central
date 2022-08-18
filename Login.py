from tkinter import *
import sqlite3
from Cadastrar_técnico import cadastro_tecnico
from Central import central

dsn = {   'fonte1': 'Franklin 25 bold',
          'fonte2': 'Yu 15',
          'fonte3': 'Arial 12',
          'laranja1': '#F76A57',
          'preto': '#2e2e2d',
          'branco':'#fafafa',
          'branco2': 'white',
          'laranja2': '#F4D9D7',
          'branco3':'#f5eae6',
          'relif': FLAT,
          'y_dist': 10,
          'x_dist': 20,         }

login = Tk()

# centralizando a tela
janela_altura = 350
janela_largura = 400
tela_larg = login.winfo_screenwidth()
tela_alt = login.winfo_screenheight()
x = int((tela_larg / 2) - (janela_largura / 2))
y = int((tela_alt / 2.5) - (janela_altura / 2))
login.geometry(f"{janela_largura}x{janela_altura}+{x}+{y}")
login.configure()
login.resizable(False, False)


def entrar():
    try:
        # Banco
        banco = sqlite3.connect('Central-Ferramentas.db')
        cursor = banco.cursor()
        cursor.execute(f"SELECT Senha FROM técnicos WHERE Email='{entrada_email.get()}'")
        senhas=    cursor.fetchall()
        senha_bd =senhas[0][0]
        senha_digitada = entrada_senha.get()

        print(senha_bd,senha_digitada)

        if senha_digitada == senha_bd:
            central()
        else:
            print('Erro na verificação,tente novamente')
    except :
        print(f'Erro verficar entrar')

titulo = Label(login,text='Bem vindo a Central',font=dsn['fonte1'],fg=dsn['laranja1'],)

email= Label(login, text='E-mail :  ', font=dsn['fonte2'],fg=dsn['preto'])
entrada_email = Entry(login, font=dsn['fonte2'], relief=dsn['relif'],width=18)

senha=  Label(login,text='Senha :  ',font=dsn['fonte2'],)
entrada_senha= Entry(login,font=dsn['fonte2'],relief=dsn['relif'],width=18)

entrar_b = Button(login, text='Entrar',command=entrar,font=dsn['fonte2'],fg=dsn['branco'],bg=dsn['laranja1'],relief=dsn['relif'])

info= Label(login,text='Ainda não tem um cadastro? ',font='arial 12')

cadastro = Button(login,text='Cadastre-se',command=cadastro_tecnico,font=dsn['fonte3'],fg=dsn['branco'],bg=dsn['laranja1'],relief=dsn['relif'])


#posicionamento
titulo.grid(columnspan=2,column=1,row=0,pady=20,padx=40)
email.grid(column=1, row=1,pady=5,sticky='e')
entrada_email.grid(column=2,row=1,pady=5,sticky='w')
senha.grid(column=1,row=2,sticky='e')
entrada_senha.grid(column=2,row=2,pady=5,sticky='w')
entrar_b.grid(column=1, row=3, columnspan=2,pady=10 )
info.grid(column=1,row=4,columnspan=2,pady=10)
cadastro.grid(column=1,row=5,columnspan=2,)

login.mainloop()