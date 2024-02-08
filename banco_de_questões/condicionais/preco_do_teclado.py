teclado_varejo = 30
teclado_atacado = 25
while True:
    try:
        teclados_comprados = int(input('Quantos teclados foram comprados?: '))
        if teclados_comprados == 1:
            print(f'Foi gasto R$30.00 com a compra do teclado no varejo')
            break
        elif 0<teclados_comprados <12:
            print(f'Foram gastos R${(teclados_comprados*teclado_varejo):.2f} com a compra dos teclados no varejo')
            break
        elif teclados_comprados>=12:
            print(f'Foram gastos R${(teclados_comprados*teclado_atacado):.2f} com a compra dos teclados no atacado')
            break
        else:
            print('Não foi comprado nenhum teclado então')
    except:
        print('Digite apenas números inteiros')