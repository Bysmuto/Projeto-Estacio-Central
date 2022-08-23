
def centralizar(janela,altura,largura):
    # centralizando a tela
    janela_altura = altura
    janela_largura = largura
    tela_larg = janela.winfo_screenwidth()
    tela_alt = janela.winfo_screenheight()
    x = int((tela_larg / 2) - (janela_largura / 2))
    y = int((tela_alt / 2.5) - (janela_altura / 2))
    janela.geometry(f"{janela_largura}x{janela_altura}+{x}+{y}")
    janela.resizable(False, False)