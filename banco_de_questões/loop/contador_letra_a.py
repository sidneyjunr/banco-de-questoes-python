"""
Contador de letra A
Faça um programa que pede para o usuário digitar
uma frase e conte quantas letras A existem na
frase e mostre na tela a quantidade encontrada


"""

while True:
    frase = str(input('Digite uma frase: ')).lower()
    contador = 0
    for letra in frase:
        if letra in "aáàã":
            contador+=1
    print(f'Esta frase tem {contador} letras A ')
    break