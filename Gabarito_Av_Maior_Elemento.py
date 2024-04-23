def maior_elemento():
    return max(lista)

numeros = input("Digite uma lista de numeros separados por espaço: ").split()
numeros = [int(num) for num in numeros]

maior = maior_elemento(numeros)
print("O maior elemento da lista é: ", maior)
