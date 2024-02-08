"""
Removendo da Agenda

Dado o dicionário agenda = {'Ana': '555-1234', 'João':
'555-5678', 'Maria': '555-4321'}, peça para o usuário
escolher o nome de uma pessoa e remove do
dicionário a pessoa escolhida.
"""

agenda = {
    'Ana': '555-1234',
    'João': '555-5678', 
    'Maria': '555-4321'
}
print(agenda)

nome_pra_remover = str(input('Digite o nome de uma pessoa para remover: ').capitalize())

if nome_pra_remover in agenda:
    del agenda[nome_pra_remover]
else:
    print('Nome não encontrado em agenda')

print(f"\n\n\n\n Agenda Atualizada: {agenda}")