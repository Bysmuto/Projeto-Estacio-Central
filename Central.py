from tkinter import *
from Ferramentas import ferramentas
from Técnicos import tecnicos
from Cadastrar_técnico import cadastro_tecnico
from Cadastrar_Ferramentas import casdastro_ferramenta

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
          'x_dist': 10,         }

janela = Tk()
janela.geometry('550x300+400+150')
janela.config(bg=dsn['branco'])

titulo = Label(janela, text='Central de ferramentas', font=dsn['fonte1'], bg=dsn['branco'], fg=dsn['laranja1'])
titulo.grid(columnspan=2,column=1,row=1,padx=100,pady=40)

b_ferramentas = Button(janela, text='Ferramentas', command=ferramentas, font=dsn['fonte2'], bg=dsn['laranja1'], fg=dsn['branco2'], relief=dsn['relif'])
b_ferramentas.grid(column=1,row=2)

b_tecnicos = Button(janela,text='Técnicos',command=tecnicos, font=dsn['fonte2'], bg=dsn['laranja1'], fg=dsn['branco2'], relief=dsn['relif'])
b_tecnicos.grid(column=2,row=2)

b_c_tecnicos = Button(janela,text=' Cadastar Técnico',command=cadastro_tecnico, font=dsn['fonte3'], bg=dsn['laranja1'], fg=dsn['branco2'], relief=dsn['relif'])
b_c_tecnicos.grid(column=2,row=3)

b_c_ferramenta = Button(janela,text=' Cadastar Ferramenta',command=casdastro_ferramenta, font=dsn['fonte3'], bg=dsn['laranja1'], fg=dsn['branco2'], relief=dsn['relif'])
b_c_ferramenta.grid(column=1,row=3,pady=dsn['y_dist'])


janela.mainloop()




