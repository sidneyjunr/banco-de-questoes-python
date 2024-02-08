"""
Menor de 18 

Dada a lista de dicionários pessoas = [{'nome': 'Ana',
'idade': 16}, {'nome': 'João', 'idade': 30}, {'nome':
'Maria', 'idade': 17}], crie uma lista com o nome das
pessoas que possuem menos que 18 anos

"""
pessoas = [
    {'nome': 'Ana','idade': 16}, 
    {'nome': 'João', 'idade': 30}, 
    {'nome':'Maria', 'idade': 17}
]

menores = []
nomes_menores = []
for i in pessoas:
    if i['idade']<18:
        menores.append({'nome': i['nome'],'idade':i['idade']})
        nomes_menores.append(i['nome'])
print(menores)

print(f"\n\n\nPessoas com menos de 18 anos: {nomes_menores}")