"""
Atualizando estoque

Dado o dicionário estoque = {'maçã': 10, 'banana': 5,
'laranja': 8, 'uva': 12} peça para o usuário digitar o
nome e quantidade de mais 3 frutas, guarde em
um novo dicionário e atualize o estoque

"""
estoque = {
    'maçã': 10, 
    'banana': 5,
    'laranja': 8,
    'uva': 12
}
dicionario={

}
for i in range(3):
    fruta = str(input('Digite uma fruta: ').strip().lower() )
    quantidade = int(input(f'Digite a quantidade de {fruta}: ').strip())
    dicionario[fruta] = quantidade



# for i,j in dicionario.items():
#     if i not in estoque:
#         dicionario[i] = j

for i,j in estoque.items():
    if i in dicionario:
        dicionario[i] +=j
    else:
        dicionario[i] = j
        
print(f'O dicionario atualizzado=  {dicionario}  ')
        