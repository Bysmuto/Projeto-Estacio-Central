from tkinter import *
import sqlite3
from centralizar import centralizar

def casdastro_reserva():

    design = {'fonte1': 'Arial 25',
              'fonte2': 'Arial 15',
              'laranja1': '#F76A57',
              'preto': '#2e2e2d',
              'laranja2' : '#F4D9D7',
              'relif': FLAT,
              'y_dist':5,
               'x_dist':10,}

    janela = Tk()

    centralizar(janela,400,400)

    titulo = Label(janela, text='Cadastrar Reserva', font=design['fonte1'], fg=design['laranja1'])
    titulo.grid(column=0, row=0, columnspan=2, pady=10,padx=10)

    nomes = ('Ferramenta:',
             'Id F :',
             'Técnico :',
             'Id T :',
             'tempo :',
             'inicio :',
             'entrega :',
             )

    cords_y =(range(1, len(nomes) + 1))

    for n, c in zip(nomes, cords_y):
        nome = Label(janela, text=n, font=design['fonte2'], fg=design['preto'],)
        nome.grid(column=0, row=c,sticky=W,pady=design['y_dist'],padx=design['x_dist'])


    Ferramenta  = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'], bg=design['laranja2'])
    IdF         = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'], bg=design['laranja2'])
    Tecnico     = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'], bg=design['laranja2'])
    IdT         = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'],bg=design['laranja2'])
    tempo    = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'], bg=design['laranja2'])
    inicio     = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'], bg=design['laranja2'])
    entrega   = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'], bg=design['laranja2'])

    entradas_f = (Ferramenta,
                  IdF,
                  Tecnico,
                  IdT,
                  tempo,
                  inicio,
                  entrega,
                  )


    for e, c in zip(entradas_f, cords_y):
        e.grid(column=1, row=c,padx=design['x_dist'],pady=design['y_dist'])

    def cadastro():
        banco = sqlite3.connect('Central-Ferramentas.db')
        cursor = banco.cursor()

        pegar_entradas = [ent.get() for ent in entradas_f]
        print(pegar_entradas)

        quant_valores = '?,' * (len(entradas_f)-1) + '?'
        print(quant_valores)
        cursor.execute(f"INSERT OR IGNORE INTO Reservas VALUES({quant_valores})", (pegar_entradas))

        banco.commit()
        banco.close()
        print(f'Reserva {Ferramenta.get()} reservada')
        janela.destroy()

        # update na tabela
        # ferramentas_tabela.destroy()
        # tabela()

    cadastrar = Button(janela, text='Enviar', command=cadastro, font=design['fonte2'], fg=design['laranja1'],
                       relief=design['relif'])

    cadastrar.grid(column=0, row=len(nomes)+1, columnspan=2, pady=design['y_dist'])

    janela.mainloop()

if __name__=='__main__':
    #erro é normal, so é possivel enviar usando todas as janelas
    casdastro_reserva()