"""
Média das Notas

Dada a lista notas = [7.5, 8.0, 9.5, 6.0, 8.5], calcule a
média das notas e imprima o resultado.
"""

notas = [7.5, 8.0, 9.5, 6.0, 8.5]

print(f' A média das notas é : {sum(notas)/len(notas)}')


notas_somadas= 0
for nota in notas:
    notas_somadas+=nota

media = notas_somadas/5
print(f'A média das notas é {media}')