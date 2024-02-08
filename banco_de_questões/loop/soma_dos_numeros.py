"""
Soma dos números
Faça um programa que pede para o usuário digitar
10 números e mostre na tela a soma de todos os
números digitados

"""
soma = 0

for i in range(1,11):
    while True:
        try:
            num= float(input(f'Digite o {i}º número: '))
            soma += num
            break
        except:
            print('ISTO NÂO É UM NÚMERO')
print(f'A soma dos 10 números é: {soma}')