"""
Melhor alunos

Dado o dicionário notas_alunos = {'Ana': [8.0, 7.5,
9.0], 'João': [7.0, 8.5, 9.5], 'Maria': [9.0, 8.0, 8.5]},
mostre na tela o nome e a média do aluno que
possui as melhores notas.

"""

notas_alunos = {
    'Ana': [8.0, 7.5,9.0],
    'João': [7.0, 8.5, 9.5],
    'Maria': [9.0, 8.0, 8.5]
}
resultado ={}

for i,j in notas_alunos.items():
    media = sum(j)/len(j)

    resultado[i] = media

# for i,j in resultado.items(): 
maior_media = max(resultado, key=resultado.get)
print(f'O aluno com a maior média é {maior_media} com média {resultado[maior_media]:.2f}')