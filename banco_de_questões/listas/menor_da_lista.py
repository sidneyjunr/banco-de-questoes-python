"""
Menor da Lista

Crie uma lista chamada números, peça para o
usuário inserir 5 números e alimente essa lista,
depois mostre o menor número dessa lista

"""

numeros = []

for i in range(1,6):
    while True:
        try:
            numero = float(input(f'Digite o {i} número: '))
            numeros.append(numero)
            break
        except:
            print('Isto não é um número')

menor_numero = numeros[0]

for numero in numeros:
    if numero < menor_numero:
        menor_numero = numero

print(f'O menor número da lista é o {menor_numero}')