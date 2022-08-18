from tkinter import *
import sqlite3

def cadastro_tecnico():
    design = {'fonte1': 'Franklin 25 bold',
              'fonte2': 'Franklin 16 bold',
              'laranja1': '#F76A57',
              'preto': '#2e2e2d',
              'laranja2' : '#fad8cd',
              'branco':'#fafafa',
              'branco3':'#f5eae6',
              'relif': FLAT,
              'y_dist':5,
               'x_dist':20,}

    janela_ct = Tk()
    janela_ct.config(bg=design['branco'])
    # centralizando a tela
    janela_altura = 420
    janela_largura = 370
    tela_larg = janela_ct.winfo_screenwidth()
    tela_alt = janela_ct.winfo_screenheight()
    x = int((tela_larg / 2) - (janela_largura / 2))
    y = int((tela_alt / 2.5) - (janela_altura / 2))
    janela_ct.geometry(f"{janela_largura}x{janela_altura}+{x}+{y}")

    titulo = Label(janela_ct, text='Cadastro', font=design['fonte1'], fg=design['laranja1'],bg=design['branco'])
    titulo.grid(column=0, row=0, columnspan=3, pady=10,padx=20)

    nomes = ('Nome:'   ,
             'Cpf:'    ,
             'Senha:'  ,
             'E-mail:' ,
             'Contato:',
             'Turno:'  ,
             'Equipe:',)

    cord_y = (range(1, len(nomes)+1))

    for n, c in zip(nomes, cord_y):
        nome = Label(janela_ct, text=n, font=design['fonte2'], fg=design['preto'],bg=design['branco'])
        nome.grid(column=0, row=c,sticky='w',pady=design['y_dist'],padx=design['x_dist'])


    entrada_nome    = Entry(janela_ct, font=design['fonte2'], fg=design['preto'], relief=design['relif'], bg=design['laranja2'],width=15,)
    entrada_cpf     = Entry(janela_ct, font=design['fonte2'], fg=design['preto'], relief=design['relif'], bg=design['laranja2'],width=15)
    entrada_senha   = Entry(janela_ct, font=design['fonte2'], fg=design['preto'], relief=design['relif'], bg=design['laranja2'],width=15)
    entrada_email   = Entry(janela_ct, font=design['fonte2'], fg=design['preto'], relief=design['relif'], bg=design['laranja2'],width=15)
    entrada_contato = Entry(janela_ct, font=design['fonte2'], fg=design['preto'], relief=design['relif'], bg=design['laranja2'],width=15)
    entrada_turno   = Entry(janela_ct, font=design['fonte2'], fg=design['preto'], relief=design['relif'], bg=design['laranja2'],width=15)
    entrada_equipe  = Entry(janela_ct, font=design['fonte2'], fg=design['preto'], relief=design['relif'], bg=design['laranja2'],width=15)
    entrada_equipe  = Entry(janela_ct, font=design['fonte2'], fg=design['preto'], relief=design['relif'], bg=design['laranja2'],width=15)


    entradas_t =[entrada_nome    ,
                 entrada_cpf     ,
                 entrada_senha   ,
                 entrada_email   ,
                 entrada_contato ,
                 entrada_turno   ,
                 entrada_equipe  ,]

    for e, c in zip(entradas_t, cord_y):
        e.grid(column=1, row=c,padx=design['x_dist'],pady=design['y_dist'],sticky='w')

    def cadastro():
        banco = sqlite3.connect('Central-Ferramentas.db')
        cursor = banco.cursor()

        pegar_entradas = [ent.get() for ent in entradas_t]+[None]

        quant_valores = '?,' * len(entradas_t) + '?'
        cursor.execute(f"INSERT OR IGNORE INTO técnicos VALUES ({quant_valores}) ", (pegar_entradas))

        banco.commit()
        banco.close()
        print(f'Usuario {entrada_nome.get()} cadastrado')
        janela_ct.destroy()


    cadastrar = Button(janela_ct, text='Enviar', command=cadastro, font='Franklin 16 ', fg=design['branco'],bg=design['laranja1'],
                       relief=design['relif'])
    cadastrar.grid(column=0, row=len(nomes)+1, columnspan=2, pady=15)


    janela_ct.mainloop()

if __name__=='__main__':
    cadastro_tecnico()