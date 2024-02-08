"""
Ordenando

Dada a lista de dicionários alunos = [{'nome': 'Ana',
'nota': 8.5}, {'nome': 'João', 'nota': 7.0}, {'nome':
'Maria', 'nota': 9.5}], ordene a lista com base nas
notas em ordem decrescente.

"""

alunos = [
{'nome': 'Ana','nota': 8.5},
{'nome': 'João', 'nota': 7.0},
{'nome':'Maria', 'nota': 9.5}
]

alunos.sort(key=lambda x:x["nota"], reverse=True)

for i in alunos:
    print(i)