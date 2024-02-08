while True:
    try:
        nota1 = int(input('Digite a primeira nota: '))
        if 10>=nota1>=0:
            while True:
                try:
                    nota2 = int(input('Digite a segunda nota: '))
                    if 10>=nota2>=0:
                        while True:
                            try:
                                nota3 = int(input('Digite a terceira nota: '))
                                if 10>=nota3>=0:
                                    media = (nota1+nota2+nota3)/3

                                    if media>=7:
                                        print(f'Aprovado com média{media}')
                                        break
                                    elif media<7:
                                        print(f'Reprovado com média{media}')
                                        break
                                else:
                                    print('3º nota inválida, somente notas entre 0 e 10')
                            except:
                                print('Digite apenas números ')
                    else:
                        print('2º nota inválida, somente notas entre 0 e 10')
                except:
                    print('Digite apenas números')
        else:
            print('1º nota inválida, somente notas entre 0 e 10')
    except:
        print('Digite apenas números')
        