# Projeto: Utilidades para tela do terminal
# Data: 01/08/2021
# License: GNU GENERAL PUBLIC LICENSE - Version 3, 29 June 2007
# Fabiano Stussi Pereira® - © 2021

import os
import platform


def limpa_tela():
    os.system('cls' if platform.system() == 'Windows' else 'clear')


def desenha_linha(simbolo: str, tamanho=10):
    print(simbolo * tamanho)


def titulo(texto: str, simbulo='*'):
    texto = f'** {texto} **'
    desenha_linha(f'{simbulo}', len(texto))
    print(texto)
    desenha_linha(f'{simbulo}', len(texto))


def titulo_ml(titulos: list, alinhamento='e'):
    maior_texto = max(map(lambda item: len(item), titulos))
    desenha_linha('=', maior_texto + 4)
    for texto in titulos:
        if alinhamento == 'c':
            print(f'| {texto: ^{maior_texto}} |')
        else:
            print(f'| {texto: <{maior_texto}} |')
    desenha_linha('=', maior_texto + 4)


def cria_menu(menu: list):
    maior_texto = max(map(lambda item: len(item), menu))
    desenha_linha('=', maior_texto + 9)
    for i, item in enumerate(menu):
        print(f'| {i + 1:>2} - {item: <{maior_texto}} |')
    desenha_linha('=', maior_texto + 9)


if __name__ == '__main__':
    pass
