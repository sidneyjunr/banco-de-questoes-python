while True:
    try:
        num1 = int(input('Digite um número inteiro: '))
        
        if num1 == 0:
            print('Este um número neutro')
            break
        elif num1 > 0 :
            print('Este é um número positivo')
            break
        else:
            print('Este é um número negativo')
            break
    except:
        print('Digite um número inteiro')