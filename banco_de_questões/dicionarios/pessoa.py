"""
Pessoa

Crie um dicionário chamado pessoa com as chaves
'nome', 'idade', 'altura' e 'cidade'. Peça para o
usuário preencher os dados e imprima o dicionário

"""

pessoa = {}
while True: 
    pessoa["nome"] = str(input('Digite seu nome: '))
    if pessoa["nome"].replace(' ','').isalpha():
        break
    else:
        print('Digite somente letras')
while True: 
        try:
            pessoa["idade"] = int(input('Digite sua idade: '))
            if pessoa['idade']>0:
                 break
            else:
                 print('Digite uma Idade Real')
                 continue
        except:
             print('Digite um número inteiro')

while True:
    try:
        pessoa['altura'] = float(input('Digite sua altura(em metros): ').replace(',','.'))
        if pessoa['altura'] <= 0 :
             print('Coloque uma altura válida')
        elif pessoa['altura']> 2.3:
             print('Você é um gigante, só pode')
        else:
            break
    except:
         print('Isto não é um número')

while True: 
    pessoa['cidade'] = str(input('Digite sua cidade: '))
    if pessoa["cidade"].replace(' ','').isalpha():
        break
    else:
        print('Digite somente letras')
print('======= DADOS DA PESSOA ======')
print(f'Nome: {pessoa['nome']}')
print(f'Idade: {pessoa['idade']}')
print(f'Altura: {pessoa['altura']:.2f}m')
print(f'Cidade: {pessoa['cidade']}')