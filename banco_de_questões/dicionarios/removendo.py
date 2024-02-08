"""
Removendo

Dado o dicionário estoque = {'maçã': 10, 'banana': 5,
'laranja': 8, 'uva': 12}, remova a entrada
correspondente à 'laranja' e imprima o dicionário
atualizado.

"""
estoque = {
'maçã': 10,
'banana': 5,
'laranja': 8,
'uva': 12
}

del estoque['laranja']
print(f"Dicionário de Estoque Atualizado: {estoque}")