"""
Lista Infinita

Escreva um programa que solicite ao usuário para
inserir palavras até que ele digite "sair". Armazene
essas palavras em uma lista e, em seguida,
imprima a maior palavra que foi digitada.

"""

palavras = []

while True:
    palavra = input('Digite uma palavra: ').capitalize().strip()

    if palavra == 'Sair':
        break
    palavras.append(palavra)
if palavras:
    maior_comprimento = len(palavras[0])

    for palavra in palavras:
        if len(palavra) > maior_comprimento:
            maior_comprimento = len(palavra)    
            maior_palavra=palavra

    print(f'A maior palavra é "{maior_palavra}" com {maior_comprimento} letras')
else:
    print('Nenhuma palavra foi digitada')