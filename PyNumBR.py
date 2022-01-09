# Projeto: Utilidades para tela do terminal
# Data: 01/08/2021
# License: GNU GENERAL PUBLIC LICENSE - Version 3, 29 June 2007
# Fabiano Stussi Pereira® - © 2021

from datetime import datetime
import locale


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def ler_inteiro(msg: str,
                msg_erro='[Erro de tipo] É esperado um número inteiro,' +
                'tente novamente') -> int:
    while True:
        try:
            inteiro = int(input(msg))
        except ValueError:
            print(msg_erro)
            continue
        return inteiro


def ler_real(msg: str,
             msg_erro='[Erro de tipo] É esperado um número real,' +
             'tente novamente') -> float:
    while True:
        numero = input(msg).replace(',', '.')
        try:
            real = float(numero)
        except ValueError:
            print(msg_erro)
            continue
        return real


def mostra_real(num_float: float) -> str:
    return locale.format_string('%.2f', num_float, grouping=True)


def pega_data() -> str:
    return datetime.now().strftime('%d/%m/%Y')


def pega_hora() -> str:
    return datetime.now().strftime('%H:%M')


if __name__ == '__main__':
    print(pega_data())
