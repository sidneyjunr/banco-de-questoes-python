"""
Ordem Crescente

Dada a lista produtos =[
    ('Mouse', 25.99),
    ('Teclado',59.99),
    ('Mousepad', 15.99),
    ("Monitor", 600.00),
    ("Fone de Ouvido", 110.50)
    ],
ordene a lista com base
no segundo elemento de cada tupla (o preço) em
ordem crescente.

"""

lista_produtos =[
    ('Mouse', 25.99),
    ('Teclado',59.99),
    ('Mousepad', 15.99),
    ("Monitor", 600.00),
    ("Fone de Ouvido", 110.50)
    ]

lista_produtos.sort(key=lambda x:x[1])
print(lista_produtos)   

