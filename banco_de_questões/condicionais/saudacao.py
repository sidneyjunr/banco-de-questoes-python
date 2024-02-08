while True:
    while True:
        nome = str(input('Digite seu nome: ')).capitalize()
        tem_numero = False
        for letra in nome:
            if letra.isdigit():
                tem_numero = True
        if tem_numero is True:
            print('Digite apenas letras')
        else:
            break    

    while True:
        hora = int(input("Digite a hora [0] às [23]: "))

        if 0<=hora<24:
            if 12>hora>=6:
                print(f'Bom dia {nome}')
                break
            elif 18>hora>=12:
                print(f'Boa tarde {nome}')
                break
            else:
                print(f'Boa noite {nome}')
                break
        else:
            print('Hora inválida')
    break