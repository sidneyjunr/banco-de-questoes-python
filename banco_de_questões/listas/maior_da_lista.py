"""
Maior da Lista

Crie uma lista chamada números, peça para o
usuário inserir 5 números e alimente essa lista,
depois mostre o maior número dessa lista.

"""

numeros= []

for i in range(1,6):
    while True:
        try:
            numero = float(input(f'Digite o {i}º numero: '))
            numeros.append(numero)
            break
        except:
            print('Isto não é um número')
maior_numero = numeros[0]
for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero

print(f'O maior número da lista é o {maior_numero}')