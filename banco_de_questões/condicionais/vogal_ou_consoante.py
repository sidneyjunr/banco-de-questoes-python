while True:
    letra = input('Digite uma letra: ').lower()
    if letra ==1 and letra == '' or letra == ' ':
        print('Digite algo ué')

    elif len(letra)==1:
        if letra in 'aeiou':
            print('É vogal')
            break
        elif letra in 'abcdefghijklmnopqrstuvwxyz':
            print('É consoante')
            break
        else:
            print('Isto não é uma letra')
            
    else:
        print('Digite APENAS UMA letra :( ')