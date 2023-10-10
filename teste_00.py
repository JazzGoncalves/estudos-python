"Jogo de adivinhação de números"

import random 

def main():
    minimo = int(input("Insira o minimo númerico para a adivinhação"))
    maximo = int(input("Insira o maximo númerico para a adivinhação"))
    numero = random.randint(minimo,maximo)
    count = 0
    while True:
        count += 1
        usuario = int(input("Insira seu palpite"))
        if usuario < numero:
            print(" Número muito pequeno")
        elif usuario > numero:
            print("Número muito alto")
        else:
            print("Você realizou",count ,"tentativas")
            break 
if __name__ == "__main__":
    main()
