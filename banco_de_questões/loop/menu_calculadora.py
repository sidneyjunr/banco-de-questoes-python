"""
Menu de Calculadora

Faça um programa que pede 2 números para o
usuário e exibe um menu perguntando qual
operação matemática ele quer realizar ou se ele
quer encerrar o programa e exiba o resultado na
tela a cada escolha do usuário

"""

while True:
    try:
        menu =int(input('''
    ======CALCULADORA======
        ESCOLHA UMA OPÇÃO

        1 - SOMAR [+]
        2 - SUBTRAIR [-]
        3 - MULTIPLICAR [x]
        4 - DIVIDIR [/]

        9 - SAIR
    '''))
        match menu:
            case 1:
                while True:
                    try:
                        num1=float(input('Digite o 1º número: '))
                        break
                    except:
                        print(f'{'='*5}ERRO{'='*5}')

                while True:
                    try:
                        num2=float(input('Digite o 2º número: '))
                        break
                    except:
                        print(f'{'='*5}ERRO{'='*5}')
                print(f'{num1} + {num2} = {num1+num2}')
                
            case 2: 
                while True:
                    try:
                        num1=float(input('Digite o 1º número: '))
                        break
                    except:
                        print(f'{'='*5}ERRO{'='*5}')

                while True:
                    try:
                        num2=float(input('Digite o 2º número: '))
                        break
                    except:
                        print(f'{'='*5}ERRO{'='*5}')
                print(f'{num1} - {num2} = {num1-num2}')                
            case 3:
                while True:
                    try:
                        num1=float(input('Digite o 1º número: '))
                        break
                    except:
                        print(f'{'='*5}ERRO{'='*5}')

                while True:
                    try:
                        num2=float(input('Digite o 2º número: '))
                        break
                    except:
                        print(f'{'='*5}ERRO{'='*5}')
                print(f'{num1} x {num2} = {num1*num2}')                
            case 4:
                while True:
                    try:
                        num1=float(input('Digite o 1º número: '))
                        break
                    except:
                        print(f'{'='*5}ERRO{'='*5}')

                while True:
                    try:
                        num2=float(input('Digite o 2º número: '))
                        break
                    except:
                        print(f'{'='*5}ERRO{'='*5}')
                if num2 == 0:
                    print('Não é possivel dividir por 0')
                
                else:
                    print(f'{num1} / {num2} = {num1/num2}')
                
            case 9:
                break
            case _ :
                print('Opção inválida')
    except:
        print(f"{'='*5} Digite um NÚMERO INTEIRO {'='*5}")