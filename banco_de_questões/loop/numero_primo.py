"""
Numero Primo

Faça um programa que pede para o usuário digitar
um número inteiro e positivo e mostre na tela se ele
é ou não um número primo.

"""
while True:
    try:
        num = int(input('Digite um número inteiro e positivo: '))
        if num >=0:
            if num == 2:
                print('Este número é primo')
                break

            primo = False
            for i in range(2,num):
                if num % i == 0:
                    primo = False
                    break
                        
                else:
                    primo = True
                
            if num>0:
                if primo == True:
                    print('Este número é primo')
                    break

                elif primo == False:
                    print("Este numero não é primo")
                    break
            else:
                print('Numero igual a 0')
                break
        else:
            print('Isto é um número negtivo')
    except:
        print('Isto não é um número inteiro e positivo')