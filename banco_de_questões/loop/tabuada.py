"""
TABUADA

Faça um programa que pede 1 número inteiro
entre 1 e 10 para o usuário e mostre na tela a
tabuada desse número

"""
while True:
    try:
        num = int(input('Digite um número inteiro entre 1 e 10: '))
        if 10>=num>0:
            for i in range(1,11):
                print(f'{i} x {num} = {i*num}')
            break
        else:
            print('Este número não está entre 1 e 10')
    except:
        print('='*5,'ISTO NÃO É UM NÚMERO INTEIRO','='*5)