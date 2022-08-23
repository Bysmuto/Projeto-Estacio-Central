import sqlite3
from pandas import DataFrame
from os import startfile


def exportar_f(tabela,nome):
    banco = sqlite3.connect('Central-Ferramentas.db')
    cursor = banco.cursor()

    # itens da tabela
    elementos = '*'
    cursor.execute(f"SELECT {elementos} FROM {tabela} ")
    colunas_nomes = [nome[0] for nome in cursor.description]
    valores = cursor.fetchall()


    excel = DataFrame(valores, columns=colunas_nomes)
    excel.to_excel(f'{nome}.xlsx')
    try:
        abrir = startfile(f'{nome}.xlsx')
    except FileNotFoundError:
        print('arquivo não encontrado')
        pass

