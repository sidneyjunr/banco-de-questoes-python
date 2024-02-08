"""
Interseção

Dadas as listas [5, 1, 9, 3, 4, 7] e [1, 8, 2, 7, 5, 0] faça
uma varredura e crie uma nova lista contendo
apenas os números que estejam contidos nas duas
listas

"""

lista1 = [5, 1, 9, 3, 4, 7]

lista2 = [1, 8, 2, 7, 5, 0]

lista3 = []

for item in lista1:
    if item in lista2:
        lista3.append(item)

print(f"Números presentes em ambas as listas: {lista3}")