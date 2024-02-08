"""
Menores que 5

Dada a lista [2, 8, 15, 5, 3, 6, 1] remova todos os
elementos maiores que 5 e depois mostre a lista
atualizada.

"""

lista = [2, 8, 15, 5, 3, 6, 1]
lista_atualizada = [ num for num in lista if num <=5]

# for i in lista:
#     if i <= 5:
#         lista_atualizada.append(i)

print(f'A lista atualizada: {lista_atualizada}')