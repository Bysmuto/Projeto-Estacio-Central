from tkinter import *
import sqlite3

design = {'fonte1': 'Arial 20',
          'fonte2': 'Arial 14',
          'laranja1': '#F76A57',
          'preto': '#2e2e2d',
          'relif': FLAT, }

janela = Tk()

titulo = Label(janela, text='Cadastro', font=design['fonte1'], fg=design['laranja1'])
titulo.grid(column=1, row=0, columnspan=2, pady=10)

nomes = ('Nome'   ,
         'Cpf'    ,
         'Senha'  ,
         'E-mail' ,
         'Contato',
         'Turno'  ,
         'Equipe'  )
cords = (1, 2, 3, 4, 5, 6, 7,)

for n, c in zip(nomes, cords):
    nome = Label(janela, text=n, font=design['fonte2'], fg=design['preto'])
    nome.grid(column=1, row=c)


entrada_nome    = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'])
entrada_cpf     = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'])
entrada_senha   = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'])
entrada_email   = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'])
entrada_contato = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'])
entrada_turno   = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'])
entrada_equipe  = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'])

entradas_t =[entrada_nome    ,
             entrada_cpf     ,
             entrada_senha   ,
             entrada_email   ,
             entrada_contato ,
             entrada_turno   ,
             entrada_equipe  ,]

for e, c in zip(entradas_t, cords):
    e.grid(column=2, row=c)


def cadastro():
    banco = sqlite3.connect('Central-Ferramentas.db')
    cursor = banco.cursor()

    pegar_entradas = [ent.get() for ent in entradas_t]
    cursor.execute("INSERT OR IGNORE INTO técnicos VALUES (?,?,?,?,?,?,?)", pegar_entradas)

    banco.commit()
    banco.close()


cadastrar = Button(janela, text='Enviar', command=cadastro, font=design['fonte2'], fg=design['laranja1'],
                   relief=design['relif'])
cadastrar.grid(column=1, row=10, columnspan=2, pady=10)

janela.mainloop()