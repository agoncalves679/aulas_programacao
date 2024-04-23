from time import sleep

def soma():
  print("Bem vindo a calcula de soma.")
  sleep(1.5)
  print("Aqui você terá a opção de soma entre números inteiros ou decimais.")
  sleep(1.5)
  print("Vamos lá")
  sleep(1.5)
  num1 = float(input("Insira o primeiro número: "))
  num2 = float(input("Agora insira o segundo número: "))

  soma = num1 + num2
  resultado = soma
  sleep(1.5)
  print(f"A soma de: {num1} + {num2} = {resultado}")

soma()

# sleep, comando para retarda a exibição do print.
# linha: 
# 3 função
# 4, 6 , 8 menu
# 10, 11 solicitar os valores do usuario
# 13 calculo
# 14 variavel 
# 16 valor a ser exibido ao usuario, soma dos valores inserido!
