"""
Maior de 10

Faça um programa que pede para o usuário digitar
10 números inteiros e mostre na tela qual maior
número que foi digitado.

"""
contador = 0
for i in range(1,11):
    while True:
        try:
            num = int(input(f'Digite o {i}º número inteiro: '))
            if num > contador:
                contador = num
                
            break
            

        except:
            print('Isto não é um número inteiro')
        
print(f'O maior número inteiro foi o {contador}')