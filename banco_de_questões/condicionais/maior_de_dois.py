while True:
    num1 = input('Digite o primeiro número inteiro: ')
    if num1.isdigit():
        while True:
            num2 = input('Digite o segundo número inteiro: ')
            if num2.isdigit():    
                if num1 > num2:
                    print(f'{num1} é maior que {num2}')
                    break
                elif num1 < num2:
                    print(f'{num2} é maior que {num1}')
                    break

                else:
                    print('Os dois números são iguais')
                    break
            else:
                print('Digite um número INTEIRO')
        break
    else:
        print('Digite um número INTEIRO')