from tkinter import *
import sqlite3

design = {'fonte1': 'Arial 20',
          'fonte2': 'Arial 14',
          'laranja1': '#F76A57',
          'preto': '#2e2e2d',
          'relif': FLAT, }

janela = Tk()

titulo = Label(janela, text='Cadastrar Ferramenta', font=design['fonte1'], fg=design['laranja1'])
titulo.grid(column=1, row=0, columnspan=2, pady=10)

nomes = ('Tipo de ferramenta',
         'ID da ferramenta',
         'Fabricante',
         'Voltagem de uso',
         'Part Number',
         'Tamanho',
         'Unidade de medida',
         'Material',
         'Máximo de reserva',)
cords = (1, 2, 3, 4, 5, 6, 7, 8, 9)

for n, c in zip(nomes, cords):
    nome = Label(janela, text=n, font=design['fonte2'], fg=design['preto'])
    nome.grid(column=1, row=c)

entrada_tipo = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'])
entrada_id = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'])
entrada_Fabricante = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'])
entrada_Voltagem = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'])
entrada_Number = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'])
entrada_Tamanho = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'])
entrada_medida = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'])
entrada_Material = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'])
entrada_reserva = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'])

entradas = (entrada_tipo,
            entrada_id,
            entrada_Fabricante,
            entrada_Voltagem,
            entrada_Number,
            entrada_Tamanho,
            entrada_medida,
            entrada_Material,
            entrada_reserva,)

for e, c in zip(entradas, cords):
    e.grid(column=2, row=c)

def cadastro():
    banco = sqlite3.connect('Central-Ferramentas.db')
    cursor = banco.cursor()

    pegar_entradas = [ent.get() for ent in entradas]
    cursor.execute("INSERT OR IGNORE INTO ferramentas VALUES (?,?,?,?,?,?,?,?,?)", pegar_entradas)

    banco.commit()
    banco.close()

cadastrar = Button(janela, text='Enviar', command=cadastro, font=design['fonte2'], fg=design['laranja1'],
                   relief=design['relif'])
cadastrar.grid(column=1, row=10, columnspan=2, pady=10)

janela.mainloop()
