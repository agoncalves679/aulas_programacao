
# função de cadastro

def cadastro():
    nome = input("Digite se nome: ")
    cpf = input("Digite seu CPF: ")
    senha = input("Digite sua senha: ")
    return nome, cpf, senha

# função login

def login(usuarios):
    cpf_log = input("Digite seu CPF: ")
    senha_log = input("Digite sua senha: ")
    
    for usuario in usuarios:
        if cpf_log == usuario[1] and senha_log == usuario[2]:
            print("Login feito com sucesso!")
            return True
    print("CPF ou senha incorreto.")
    return False

# função menu

def menu():
    usuarios = []
    while True:
        print("1. Cadastrar usuário")
        print("2. Fazer login")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            novo_usuario = cadastro()
            if len(novo_usuario[1]) == 11 and novo_usuario[1].isdigit():
                usuarios.append(novo_usuario)
                print("Usuário cadastrado com sucesso!")
            else:
                print("CPF invalido.")
                
        elif opcao == "2":
            if login(usuarios):
                break
            
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida")
            
menu()

