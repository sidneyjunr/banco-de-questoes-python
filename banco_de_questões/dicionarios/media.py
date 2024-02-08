"""
Media

Crie um dicionário chamado aluno com as chaves
'nome', 'notas' e 'faltas'. A chave 'notas' deve conter
uma lista de três notas. Imprima a média das
notas

"""

aluno ={
    "nome": 'Sidney',
    "notas": [9,10,8],
    "faltas": 2
}
media = sum(aluno['notas']) / len(aluno['notas'])

print(f"Média das notas do aluno {aluno['nome']}: {media:.2f}")
