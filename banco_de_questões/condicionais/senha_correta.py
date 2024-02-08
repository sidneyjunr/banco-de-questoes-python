while True:
    senha = '123456Ab'

    senha_digita = str(input('Digite a senha: '))

    if senha_digita == senha:
        print('Acesso liberado')
        break
    else:
        print('Acesso negado')