while True:
    try:

        numero = int(input('Digite um número inteiro positivo: '))
        if numero>=0:
            break
        else:
            print('digite um número POSITIVOOO')
    except:
        print(f'{'='*6}ISTO NÃO É UM NÚMERO INTEIRO POSITIVO{'='*6}')



if numero%3 ==0 and numero%5==0:
    print('Este número é divisivel por 3 e por 5 ao mesmo tempo')
else:
    print('Este número não é divisivel por 3 e por 5 ao mesmo tempo')