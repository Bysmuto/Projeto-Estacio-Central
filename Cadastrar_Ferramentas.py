from tkinter import *
import sqlite3
from centralizar import centralizar

def casdastro_ferramenta():

    design = {'fonte1': 'Arial 20',
              'fonte2': 'Arial 14',
              'laranja1': '#F76A57',
              'preto': '#2e2e2d',
              'laranja2' : '#F4D9D7',
              'relif': FLAT,
              'y_dist':5,
               'x_dist':10,}

    janela = Tk()

    centralizar(janela,410,400)

    titulo = Label(janela, text='Cadastrar Ferramenta', font=design['fonte1'], fg=design['laranja1'])
    titulo.grid(column=0, row=0, columnspan=2, pady=10)

    nomes = ('Descrição:',
             'Fabricante :',
             'Voltagem :',
             'Part Number :',
             'Tamanho :',
             'Medida :',
             'Material :',
             'Tipo :',)

    cords_y =(range(1, len(nomes) + 1))

    for n, c in zip(nomes, cords_y):
        nome = Label(janela, text=n, font=design['fonte2'], fg=design['preto'],)
        nome.grid(column=0, row=c,sticky=W,pady=design['y_dist'],padx=design['x_dist'])


    entrada_descricao  = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'], bg=design['laranja2'])
    entrada_Fabricante = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'],bg=design['laranja2'])
    entrada_Voltagem   = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'],bg=design['laranja2'])
    entrada_Number     = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'],bg=design['laranja2'])
    entrada_Tamanho    = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'],bg=design['laranja2'])
    entrada_medida     = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'],bg=design['laranja2'])
    entrada_Material   = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'],bg=design['laranja2'])
    entrada_tipo       = Entry(janela, font=design['fonte2'], fg=design['preto'], relief=design['relif'], bg=design['laranja2'])

    entradas_f = (entrada_descricao,
                  entrada_Fabricante,
                  entrada_Voltagem,
                  entrada_Number,
                  entrada_Tamanho,
                  entrada_medida,
                  entrada_Material,
                  entrada_tipo,)


    for e, c in zip(entradas_f, cords_y):
        e.grid(column=1, row=c,padx=design['x_dist'],pady=design['y_dist'])

    def cadastro():
        banco = sqlite3.connect('Central-Ferramentas.db')
        cursor = banco.cursor()

        pegar_entradas = [ent.get() for ent in entradas_f]+[None]

        quant_valores = '?,' * len(entradas_f) + '?'
        cursor.execute(f"INSERT OR IGNORE INTO ferramentas VALUES({quant_valores})", (pegar_entradas))

        banco.commit()
        banco.close()
        print(f'Ferramenta {entrada_descricao.get()} cadastrada')
        janela.destroy()

        # update na tabela
        ferramentas_tabela.destroy()
        tabela()

    cadastrar = Button(janela, text='Enviar', command=cadastro, font=design['fonte2'], fg=design['laranja1'],
                       relief=design['relif'])

    cadastrar.grid(column=0, row=len(nomes)+1, columnspan=2, pady=design['y_dist'])

    janela.mainloop()

if __name__=='__main__':
    casdastro_ferramenta()