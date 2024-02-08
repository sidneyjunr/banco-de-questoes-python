"""
Duplicatas

Dada a lista [4, 6, 8, 5, 6, 3, 4, 7, 9, 4, 8] remova todas
as duplicatas (números repetido) e mostre a nova
lista apenas com itens únicos

"""

lista = [4, 6, 8, 5, 6, 3, 4, 7, 9, 4, 8]

lista_atualizada=[]
for numero in lista:
    if numero not in lista_atualizada:
        lista_atualizada.append(numero)

print("Nova Lista Atualizada:",lista_atualizada)