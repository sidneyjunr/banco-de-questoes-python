"""
Listas em dicionário

Dada a lista nomes = ['Ana', 'João', 'Maria', 'Pedro'], e
a lista idades = [25, 30, 22, 28], crie um dicionário
associando cada nome à sua respectiva idade.
Imprima o dicionário resultante.

"""
nomes = ['Ana', 'João', 'Maria', 'Pedro']

idades = [25, 30, 22, 28]

dicionario = {}
for i in range(len(nomes)):    
    nome = nomes[i]
    idade = idades[i]
    dicionario[nome] = idade

print(f"Dicionário de Idades: {dicionario}")