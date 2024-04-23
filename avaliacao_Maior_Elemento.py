from time import sleep

def maior_elemento():
  print("Bem vindo,")
  print("Aqui você poderá inserir valores numéricos aleatórios")
  print("e irei lhe mostrar qual o maior valor.")

  sleep(1.5)
  valores = input("Insira os valores separados por espaço: ")

  lista_valores = list(map(int, valores.split()))

  sleep(1.5)
  maior_valor = max(lista_valores)
  print(f"Entre os valores inseridos, o maior é: {maior_valor}") 

maior_elemento()

# linhas:
# sleep, comando para retarda a exibição do print.
# 3, 4, 5, 6 função e menu, respectivamente.
# 9 comando input, pra solicitar algo do usuario.
# 11 variavel lista, usei o comando list' junto com map' q é o msm que for porem simplicificado.
# 14 variavel que exibirá o maior valor da lista.
# 15 resultado para o usuario
# 17 chamando a funcao
