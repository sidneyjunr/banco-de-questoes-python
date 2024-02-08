print('='*8,'SEMÁFORO🚥','='*8)

while True:
    semaforo = str(input("Digite uma cor do semáforo: ")).lower().strip()

    if semaforo == 'vermelho':
        print('PARE 🛑')
        break
    elif semaforo == 'amarelo':
        print('ATENÇÃO 🟡')
        break
    elif semaforo == "verde":
        print('ACELERA 🟢')
        break
    else:
        print("COR INVÁLIDA")