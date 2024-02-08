while True:
    try:
        idade = int(input('Digite o ano que você nasceu: '))
        if idade<=2024:
            maioridade= 2024 - idade
            if maioridade >=18:
                print('É maior de idade, já pode ser preso')
                break
            elif maioridade <18:
                print('É menor de idade, NÃO pode ser preso')
                break
            
        else:
            print('Tu nem nasceu ainda cadela')
    except:
        print("Digite números")

        