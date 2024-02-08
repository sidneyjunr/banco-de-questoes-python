"""
Média das notas

Faça um programa que pede para o usuário digitar
8 notas e no final calcula a média dessas notas
"""
soma = 0
for i in range(1,9):
    while True:
        try:
            num = int(input(f'Digite a {i} nota: '))
            if 10>=num>=0:
                soma +=num
                break
            else:
                print('Só existe nota de 0 a 10')
        except:
            print("Isto não é um número")
media = soma/8
print(f'A média das 8 notas é: {media}')