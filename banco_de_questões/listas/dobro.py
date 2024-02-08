"""
Dobro

Crie uma lista chamada números, peça para o
usuário inserir 5 números e alimente essa lista,
depois mostre o dobro de todos os números na
tela de forma separada

"""

numeros = []

for i in range(1,6):
    while True:
        try:
            numero = float(input(f'Digite o {i}º numero: '))
            numeros.append(numero)
            break
        except:
            print("ISTO NÃO É UM NÚMERO")

for numero in numeros:
    print(f"Dobro de {numero}: {2 * numero}")