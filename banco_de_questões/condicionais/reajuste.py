"""
Reajuste

Faça um programa que pede para o usuário digitar
seu salário e calcule o reajuste dele baseado em
quando ele ganha: abaixo de 5.000 reajuste de 15%,
entre 5.000 e 10.000 reajuste de 10% acima de
10.000 reajuste de 5%
"""
while True:
    try:
        salario = input('Digite seu salário: ').replace(',','.').strip()
        salario = float(salario)
        if salario>0:
            if salario < 5000:
                salario = salario+(salario*(15/100))
                print(f'Seu salário com reajuste é: R${salario:.2f}')
                break
            elif 10000>= salario >= 5000:
                salario = salario+(salario*(10/100))
                print(f'Seu salário com reajuste é: R${salario:.2f}')
                break
            elif salario>10000:
                salario = salario+(salario*(5/100))
                print(f'Seu salário com reajuste é: R${salario:.2f}')
                break
        else:
            print('Você está sendo escravizado')
    except:
        print('Digite apenas números')
