def verificar_pares(lista):
    pares = [num for num in lista if num % 2 == 0]
    return pares

numeros = input("Digite uma lista de numeros separados por espaço: ").split()
numeros = [int(num) for num in numeros]

pares = verificar_pares(numeros)
print("Os números pares da lista são: ", pares)

