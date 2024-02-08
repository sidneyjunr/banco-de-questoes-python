while True:
    try:
        num1= int(input('Digite o 1º número inteiro: '))
        break
    except:
        print('ISTO NÃO É UM NÚMERO INTEIRO')

while True:
    try:
        num2= int(input('Digite o 2º número inteiro: '))
        break
    except:
        print('ISTO NÃO É UM NÚMERO INTEIRO')

while True:
    try:
        num3= int(input('Digite o 3º número inteiro: '))
        break
    except:
        print('ISTO NÃO É UM NÚMERO INTEIRO')
    
if num1>num2 and num1>num3:
    print(f'{num1} é maior que {num2} e {num3}')

elif num2>num1 and num2>num3:
    print(f'{num2} é maior que {num1} e {num3}')

elif num3>num1 and num3>num2:
    print(f'{num3} é maior que {num1} e {num2}')

else:
    print('Os maiores números são iguais')
