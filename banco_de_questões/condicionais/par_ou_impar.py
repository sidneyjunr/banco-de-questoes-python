while True:
    try:

        num = int(input('Digite um número inteiro positivo: '))
        if num >= 0:

            if num%2 == 0:
                print(f'{num} é PAR')
                break
            elif num%2==1:
                print(f'{num} é IMPAR')
                break
            else:
                print(f'{num} é NEUTRO')
                break
        else:
            print('Número negativo')

    except:
        print('Número inválido')