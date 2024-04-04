from time import sleep
import math

def area(raio):
    return math.pi*raio**2

def perimetro(raio):
    return 2 * math.pi*raio

def menu():
  
  raio = float(input("Insira o raio."))
  
  while True:
    sleep(2)
    print("1. Calcular área: ")
    print("2. Calcular perímetro: ")
    print("3. Sair")
    
    opcao = input("Escolha uma opção.")
    sleep(2)
    print("Você escolheu a opção: ",opcao)
    sleep(2)
    if opcao == '1':
      a = area(raio)
      print(f'A área do circulo é: {a:.2f}')
    elif opcao == '2':
      p = perimetro(raio)
      print(f'O perimetro do círculo é: {p:.2f}')
    elif opcao == '3':
      print("Saindo...")
      break
    else:
      print("Opção inválida.")
      sleep(2)
      menu()

menu()
