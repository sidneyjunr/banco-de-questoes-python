"""
5 números

Crie uma lista chamada números, peça para o
usuário inserir 5 números e alimente essa lista,
depois mostre todos os números na tela de forma
sepada.

"""

numeros = []

for i in range(1,6):
    while True:
        try:
            numero = int(input(f'Digite o {i}º número: '))
            numeros.append(numero)
            break
        except:
            print('Isto não é um número inteiro')

for i in numeros:
    print(i)