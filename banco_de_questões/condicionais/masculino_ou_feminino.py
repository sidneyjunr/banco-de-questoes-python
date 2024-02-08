while True: 
    sexo = input('Digite uma letra [M] ou [F]: ').upper()

    if sexo == 'M':
        print("Masculino")
        break
    elif sexo == 'F':
        print("Feminino")
        break
    else:
        print('Opção inválida')