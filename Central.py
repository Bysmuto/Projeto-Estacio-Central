from tkinter import *
from tkinter import ttk
from Ferramentas import ferramentas
from Técnicos import tecnicos



dsn = {   'fonte1': 'Franklin 25 bold',
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

def central():
    janela_p = Tk()

    # centralizando a tela
    janela_altura = 300
    janela_largura = 600
    tela_larg = janela_p.winfo_screenwidth()
    tela_alt = janela_p.winfo_screenheight()
    x = int((tela_larg / 2) - (janela_largura / 2))
    y = int((tela_alt / 2.5) - (janela_altura / 2))
    janela_p.geometry(f"{janela_largura}x{janela_altura}+{x}+{y}")
    janela_p.resizable(False, False)


    janela_p.config(bg=dsn['branco'])


    titulo = Label(janela_p, text='Central de Ferramentas', font=dsn['fonte1'], bg=dsn['branco'], fg=dsn['laranja1'])
    titulo.grid(columnspan=2,column=1,row=1,padx=100,pady=40)

    b_ferramentas = Button(janela_p, text='Ferramentas', command=ferramentas, font=dsn['fonte2'], bg=dsn['laranja1'], fg=dsn['branco2'], relief=dsn['relif'])
    b_ferramentas.grid(column=1,row=2,pady=dsn['y_dist'])

    b_tecnicos = Button(janela_p, text='Técnicos', command=tecnicos, font=dsn['fonte2'], bg=dsn['laranja1'], fg=dsn['branco2'], relief=dsn['relif'])
    b_tecnicos.grid(column=2,row=2,pady=dsn['y_dist'])


    janela_p.mainloop()



if __name__=='__main__':
    central()
