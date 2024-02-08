"""
Media dos alunos

Dada a lista alunos = [{'nome': 'Ana'
,
'notas': [8.0, 7.5,
9.0]}, {'nome': 'João'
,
'notas': [7.0, 8.5, 9.5]}, {'nome':
'Maria'
,
'notas': [9.0, 8.0, 8.5}]}, crie uma lista com a
média de todos os alunos e mostre na tela em
ordem crescente

"""
alunos = [
    {'nome': 'Ana','notas': [8.0, 7.5,9.0]},
    {'nome': 'João','notas': [7.0, 8.5, 9.5]},
    {'nome':'Maria','notas': [9.0, 8.0, 8.5]}
]
media = {}
for i in alunos:
    calc_media = sum(i['notas'])/len(i['notas'])
    media[i['nome']] = calc_media



for i in sorted(media, key=media.get):
    print(i,media[i])