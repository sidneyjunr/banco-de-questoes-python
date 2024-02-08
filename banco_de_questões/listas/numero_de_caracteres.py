"""
Número de Caractéres

Dada a lista palavras = ['python', 'java', 'c++',
'javascript'], crie uma nova lista contendo o número
de caracteres de cada palavra. Imprima a lista
resultante item por item.

"""
palavras = ['python', 'java', 'c++','javascript']

palavras_len = []

for palavra in palavras:
    palavras_len.append(len(palavra))

for i in palavras_len:
    print(i)


