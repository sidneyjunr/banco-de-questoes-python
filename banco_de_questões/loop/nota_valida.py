"""
Nota válida

Faça um programa que pede para o usuário uma
nota, entre zero e dez. Mostre uma mensagem
caso o valor seja inválido e continue pedindo até
que o usuário informe um valor válido.

"""

while True:
    try:
        nota = int(input("Digite uma nota entre 0 e 10: "))
        if 10>=nota>=0:
            print('Nota válida')
            break
        else:
            print('Nota INválida')
    except:
        print('Isto não é um número inteiro')

    