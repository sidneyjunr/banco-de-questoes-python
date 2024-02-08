"""
Pares e Ímpares

Faça um programa que pede 10 números inteiros
para o usuário, calcule e mostre a quantidade de
números pares e a quantidade de números
ímpares

"""

par = 0
impar = 0
for i in range(1,11):
    while True:
        try:
            num = int(input(f'Digite o {i}º número:'))
            break
        except:
            print('Isto não é um número inteiro :/')

    if num == 0:
        ...
    elif num % 2 ==0:
        par +=1
    elif num %2 ==1:
        impar +=1
print(f'Tem {par} numeros par e {impar} numeros impar')