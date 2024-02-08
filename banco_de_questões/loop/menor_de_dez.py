"""
Menor de dez

Faça um programa que pede para o usuário digitar
10 números inteiros e mostre na tela qual menor
número que foi digitado.
"""
while True:
    try:  
        num = int(input(f'Digite o 1º número inteiro: '))
        break
    except:
        print('Isto não é um número inteiro')
menor_numero = num
for x in range(2,11):
    while True:
        try:
            num = int(input(f'Digite o {x}º número inteiro: '))
        except:
            print('Isto não é um número inteiro')
            continue
        if num < menor_numero:
            menor_numero=num
        break
print(f'O menor número digitado foi o {menor_numero}')