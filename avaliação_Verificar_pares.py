def verificar_pares():
  print("Bem vindo,")
  print("Aqui você poderá inserir valores numéricos aleatórios")
  print("e irei lhe mostrar quais são pares.")

  numeros = (input("Insira os valores separados por espaço: ")).split()

  numeros = [int(numero) for numero in numeros]

  pares = [numero for numero in numeros if numero %2 ==0]
  print("Números pares: ", pares)

verificar_pares()

# linhas
# 3, 4, 5, 6 função e menu respectivamente
# 8 pedido os numeros ao usuario
# 10 lista dos numeros inseridos, com limitação inteiros
#12 filtrando na lista somente os numeros pares, 