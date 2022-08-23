from tkinter import *
from tkinter import ttk
from Ferramentas import ferramentas_tabela
from Técnicos import tecnicos



dsn = {   'fonte1': 'Franklin 25 bold',
          'fonte2': 'Yu 25 roman',
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
    janela_altura = 400
    janela_largura = 450
    tela_larg = janela_p.winfo_screenwidth()
    tela_alt = janela_p.winfo_screenheight()
    x = int((tela_larg / 2) - (janela_largura / 2))
    y = int((tela_alt / 2.5) - (janela_altura / 2))
    janela_p.geometry(f"{janela_largura}x{janela_altura}+{x}+{y}")
    janela_p.resizable(False, False)


    janela_p.config(bg=dsn['branco'])


    titulo = Label(janela_p, text='Central de Ferramentaria', font=dsn['fonte2'], bg=dsn['branco'], fg=dsn['laranja1'],)
    titulo.grid(column=1,row=1,pady=40,padx=50,)

    b_ferramentas = Button(janela_p, text='Ferramentas', command=ferramentas_tabela, font=dsn['fonte1'], bg=dsn['laranja1'], fg=dsn['branco2'], relief=dsn['relif'])
    b_ferramentas.grid(column=1,row=2,pady=dsn['y_dist'])

    b_tecnicos = Button(janela_p, text='Técnicos', command=tecnicos, font=dsn['fonte1'], bg=dsn['laranja1'], fg=dsn['branco2'], relief=dsn['relif'])
    b_tecnicos.grid(column=1,row=3,pady=dsn['y_dist'])


    janela_p.mainloop()



if __name__=='__main__':
    central()
