agenda2 = {}

def add_contato():
    nome = input("Digite o nome: ").isalpha()
    telefone = int(input("Digite o telefone do contato: "))
    agenda2[nome] = telefone

def remover_contato():
    nome = input("Digite o nome do contato a ser removido: ")
    if nome in agenda2:
        del agenda2[nome]
        print("Contato deletado com sucesso!")
    else: 
        print("Contato inexistente!")
        
def atualizar_contato():
    nome = input("Digite o nome do contato a ser atualizado ")
    if nome in agenda2:
        telefone = input("Digite o novo telefone!")
        agenda2[nome] = telefone
        print("Informações atualizadas com sucesso")
    else:
        print("Esse contato não existe!")
        
def exibir_contatos():

def menu():
  while True:
    print("1. Adicionar Contato: ")
    print("2. Remover Contato: ")
    print("3. Atualizar Contato: ")
    print("4. Exibir Contatos: ")

    op = input("Escolha uma Opção: ")
    if op == "1":
      add_contato()

    elif op == "2":
      remover_contato()

    elif op == "3":
      atualizar_contato()

    elif op == "4":
      exibir_contatos()

    else:
      print("Opção invalida!")
    menu()

menu()

