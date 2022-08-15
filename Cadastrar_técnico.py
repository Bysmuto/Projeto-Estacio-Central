from tkinter import *
import sqlite3

design = {'fonte1': 'Arial 20',
          'fonte2': 'Arial 14',
          'laranja1': '#F76A57',
          'preto': '#2e2e2d',
          'laranja2' : '#F4D9D7',
          'relif': FLAT,
          'y_dist':5,
           'x_dist':10,}

janela = Tk()

titulo = Label(janela, text='Cadastro', font=design['fonte1'], fg=design['laranja1'])
titulo.grid(column=0, row=0, columnspan=2, pady=10)

nomes = ('Nome'   ,
         'Cpf'    ,
         'Senha'  ,
         'E-mail' ,
         'Contato',
         'Turno'  ,
         'Equipe',)

cord_y = (range(1, len(nomes)+1))

for n, c in zip(nomes, cord_y):
    nome = Label(janela, text=n, font=design['fonte2'], fg=design['preto'])
    nome.grid(column=0, row=c,sticky=W,pady=design['y_dist'],padx=design['x_dist'])


entrada_nome    = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'],bg=design['laranja2'])
entrada_cpf     = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'],bg=design['laranja2'])
entrada_senha   = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'],bg=design['laranja2'])
entrada_email   = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'],bg=design['laranja2'])
entrada_contato = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'],bg=design['laranja2'])
entrada_turno   = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'],bg=design['laranja2'])
entrada_equipe  = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'],bg=design['laranja2'])
entrada_equipe  = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'],bg=design['laranja2'])

entradas_t =[entrada_nome    ,
             entrada_cpf     ,
             entrada_senha   ,
             entrada_email   ,
             entrada_contato ,
             entrada_turno   ,
             entrada_equipe  ,]

for e, c in zip(entradas_t, cord_y):
    e.grid(column=1, row=c,padx=design['x_dist'],pady=design['y_dist'])

def cadastro():
    banco = sqlite3.connect('Central-Ferramentas.db')
    cursor = banco.cursor()

    pegar_entradas = [ent.get() for ent in entradas_t]
    cursor.execute("INSERT OR IGNORE INTO técnicos VALUES (?,?,?,?,?,?,?)", pegar_entradas)

    banco.commit()
    banco.close()
    print(f'Usuario {entrada_nome.get()}|cpf:{entrada_cpf.get()}| cadastrado')


cadastrar = Button(janela, text='Enviar', command=cadastro, font=design['fonte2'], fg=design['laranja1'],
                   relief=design['relif'])
cadastrar.grid(column=0, row=len(nomes)+1, columnspan=2, pady=10)

janela.mainloop()