while True:
    try:
        dia = int(input("Escreva um número inteiro entre 1 e 7: "))

        if dia == 1:
            print('Domingo')
            break
        elif dia ==2:
            print('Segunda')
            break
        elif dia ==3:
            print('Terça-Feira')
            break
        elif dia ==4:
            print('Quarta-Feira')
            break
        elif dia ==5:
            print('Quinta-Feira')
            break
        elif dia ==6:
            print('Sexta-Feira')
            break
        elif dia ==7:
            print('Sábado')
            break
        else: 
            print(f'{dia} não está entre 1 e 7')
    except:
        print('Digite UM NÚMEROOOOOO INTEIROOOO')