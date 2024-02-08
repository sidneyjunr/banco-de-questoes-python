"""
Soma de 1 a 500

"""
 
soma = 0

for i in range(1,501):
    print(f'{soma} + {i} = {i+soma}')
    soma +=i

print(f'A soma dos números de 1 a 500 é {soma}')