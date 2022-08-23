from tkinter import *
from tkinter import ttk
from Ferramentas import ferramentas_tabela
from Técnicos import tecnicos
from Reservas import reservas_tabela
from centralizar import centralizar



dsn = {   'fonte1': 'Franklin 25 bold',
          'fonte2': 'Yu 25 ',
          'fonte3': 'Arial 12',
          'laranja1': '#F76A57',
          'preto': '#2e2e2d',
          'branco':'#fafafa',
          'branco2': 'white',
          'laranja2': '#F4D9D7',
          'relif': 'groove',
          'y_dist': 10,
          'x_dist': 20,         }

def central():
    janela_p = Tk()
    janela_p.title('Central')

    centralizar(janela_p,400,450)

    janela_p.config(bg=dsn['branco'])


    titulo = Label(janela_p, text='Central de Ferramentaria', font=dsn['fonte2'], bg=dsn['branco'], fg=dsn['laranja1'],)
    titulo.grid(column=1,row=1,pady=30,padx=50,)

    b_ferramentas = Button(janela_p, text='Ferramentas', command=ferramentas_tabela, font=dsn['fonte1'], bg=dsn['laranja1'], fg=dsn['branco2'], relief=dsn['relif'])
    b_ferramentas.grid(column=1,row=2,pady=dsn['y_dist'])

    b_tecnicos = Button(janela_p, text='Técnicos', command=tecnicos, font=dsn['fonte1'], bg=dsn['laranja1'], fg=dsn['branco2'], relief=dsn['relif'])
    b_tecnicos.grid(column=1,row=3,pady=dsn['y_dist'])

    b_reservas = Button(janela_p, text='Reservas', command=reservas_tabela, font=dsn['fonte1'], bg=dsn['laranja1'],fg=dsn['branco2'], relief=dsn['relif'])
    b_reservas.grid(column=1, row=4, pady=dsn['y_dist'])


    janela_p.mainloop()



if __name__=='__main__':
    central()
