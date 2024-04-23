produto = {} # criou-se o dicionario 

print("Registro de produtos:") #msg para o usuario

produto["nome"] = input("Nome o produto: ") # comando para inserir 'itens' no dicionario.
produto["preco"] = float(input("Preço do produto: ")) # outro comando, para inserir valor.

print("Produto registrado:")
print("-"*20) # colocar os print entre tracinhos
print(f"Nome: {produto ['nome']}")
print(f"Preço: {produto['preco']}")
print("-"*20) # colocar os print entre tracinhos
