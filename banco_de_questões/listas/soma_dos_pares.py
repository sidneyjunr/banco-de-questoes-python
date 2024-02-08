"""
Soma dos Pares

Crie uma lista chamada números, peça para o
usuário inserir 5 números e alimente essa lista,
depois mostre a soma de todos os números pares
dessa lista

"""

numeros = []
numeros_pares = []
for i in range(1,6):
    while True:
        try:
            numero = int(input(f'Digite o {i} numero: '))
            numeros.append(numero)
            if numero%2==0:
                numeros_pares.append(numero)
            break
        except:
            print('ISTO NÃO É UM NÚMERO INTEIRO')

print(f'A soma de todos os números pares desta lista é {sum(numeros_pares)}')