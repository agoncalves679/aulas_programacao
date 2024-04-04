
import random

def game():
    n_secreto = random.randint(1, 100) #Gerar numeros interios aleatorios
    tentativas = 0
    
    while True:
        tentativa = int(input("Tente advinhar o número entre 1 e 100: "))
        tentativas += 1 # Equivalente
        
        if tentativa < n_secreto:
            print("Tente um número maior.")
        elif tentativa > n_secreto:
            print("Tente um número menor.")
        else:
            print("Parabéns! Você acertou o número em {} tentativas!".format(tentativas))
            break

game()

