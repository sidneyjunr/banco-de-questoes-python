"""
Contador de consoantes

Faça um programa que pede para o usuário digitar
uma frase e mostre na tela quantas consoantes
existem naquela frase.

"""

frase = str(input('Digite uma frase: ')).lower()
contador = 0

for letra in frase:
    if letra in 'bcdfghjklmnpqrstvwxyz':
        contador+=1

print(f'Esta frase tem {contador} consoantes')