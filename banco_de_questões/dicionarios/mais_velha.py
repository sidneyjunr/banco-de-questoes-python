"""
Mais velha

Dado o dicionário pessoas = {'João': 25, 'Maria': 30,
'Pedro': 22, 'Ana': 28}, mostre qual nome da pessoa
mais velha;

"""

pessoas = {
    'João': 25,
    'Maria': 30,
    'Pedro': 22, 
    'Ana': 28
}
velha = 0
for i,j in pessoas.items():
    if j > velha:
        velha = j
        nome = i
        
print(f'A pessoa mais velha é {nome} com {velha} anos')