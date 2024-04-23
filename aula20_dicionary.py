
#exemplos

#programa que conte a quantidade de palavras em um texto.

texto = input("Digite um texto: ")

palavras = texto.lower().split() #lower: letras minusculas. split: separar coisas.

contagem_palavras = {} #criou o dicionario.

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1
        
print("contagem de palavras no texto: ")

for palavra, quantidade in contagem_palavras.items():
    print("Palavra: ", palavra, " - Quantidade: ", quantidade)

#Exercicio
# Calculadora de Estatísticas de Alunos
#> media
#> nota mais alta
#> nota mais baixa

