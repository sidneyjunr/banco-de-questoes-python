"""
Fatorial

Faça um programa que pede para o usuário digitar
um número inteiro e positivo e mostre na tela o
fatorial desse número.

"""

num = int(input('Digite um número inteiro positivo: '))
resultado = num
for i in range(num-1,0,-1):
    fatorial = resultado*i
    print(f'{resultado} x {i} = {fatorial}')
    resultado = fatorial

print(f"""
 --------------------
       {num}! = {resultado} 
 --------------------
""")


    