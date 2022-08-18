import sqlite3
from pandas import DataFrame
from os import startfile

banco = sqlite3.connect('Central-Ferramentas.db')
cursor = banco.cursor()

# itens da tabela
tabela = 'técnicos'
cursor.execute(f"SELECT Nome,Email,Contato,Turno,Equipe,Id FROM {tabela} ")
colunas_nomes = [nome[0] for nome in cursor.description]
valores = cursor.fetchall()


def exportar_t():
    excel = DataFrame(valores, columns=colunas_nomes)
    excel.to_excel('técnicos da Central.xlsx')
    try:
        abrir = startfile('técnicos da Central.xlsx')
    except FileNotFoundError:
        print('arquivo não encontrado')
        pass

if __name__=='__main__':
    exportar_t()