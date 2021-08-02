# Projeto: Utilidades para tela do terminal
# Data: 01/08/2021
# License: GNU GENERAL PUBLIC LICENSE - Version 3, 29 June 2007
# Fabiano Stussi Pereira® - © 2021

import os
import platform


class PyUtilTerm:

    @staticmethod
    def limpa_tela():
        os.system('cls' if platform.system() == 'Windows' else 'clear')

    @staticmethod
    def desenha_linha(simbolo: str, tamanho=10):
        print(simbolo * tamanho)

    @staticmethod
    def titulo(texto: str, simbulo='*'):
        texto = f'** {texto} **'
        PyUtilTerm.desenha_linha(f'{simbulo}', len(texto))
        print(texto)
        PyUtilTerm.desenha_linha(f'{simbulo}', len(texto))

    @staticmethod
    def titulo_ml(titulos: list):
        maior_texto = len(titulos[0])
        for texto in titulos:
            tamanho_texto = len(texto) if len(texto) % 2 == 0 else len(texto) + 1
            if tamanho_texto > maior_texto:
                maior_texto = tamanho_texto
        PyUtilTerm.desenha_linha('=', maior_texto + 4)
        for texto in titulos:
            centraliza = (maior_texto - len(texto)) // 2
            print(f'|{" " * centraliza} {texto} '
                  f'{" " * centraliza if len(texto) % 2 == 0 else " " * (centraliza + 1)}|')
        PyUtilTerm.desenha_linha('=', maior_texto + 4)


if __name__ == '__main__':
    PyUtilTerm.limpa_tela()
    aviso = [
        'Desenvolvido por',
        'Fabiano Stussi Pereira',
        'Em 01/08/2021'
    ]
    PyUtilTerm.titulo_ml(aviso)
