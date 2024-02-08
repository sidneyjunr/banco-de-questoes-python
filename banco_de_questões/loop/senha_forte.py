"""
Senha Forte

Faça um programa que pede para o usuário digitar
uma senha e cheque se a senha digitada é uma
senha forte
Regras para um senha forte:
8 ou mais caracteres
Pelo menos 1 letra minúscula
Pelo menos 1 letra maiúscula
Pelo menos um caractér especial
Pelo menos 1 número
"""

senha = input('Digite a senha: ')
oito_caracteres = False
maiuscula = False
minuscula = False
especial= False
numero = False
if len(senha) >=8:
    oito_caracteres = True
    for letra in senha:
        if letra.isupper():
            maiuscula = True
        
        if letra.islower():
            minuscula = True
        
        if not letra.isalnum():
            especial = True 
        
        if letra.isdigit():
            numero = True
    if oito_caracteres and maiuscula and minuscula and especial and numero == True:
        print("Senha Forte")
    else:
        print('Senha fraca')
else:
    print('Senha fraca')