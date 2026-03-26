## Crie no algoritmo 67 as seguintes funcionalidades:
## Informe ao usuário em caso de empate.
## Crie uma forma de não permitir que um jogador jogue no mesmo lugar que já tenha uma jogada realizada.
## Atualmente o jogo encerra com o vencedor, ele agora também deve encerrar em caso de empate.
## Ao finalizar o jogo deve ser informado ao usuário uma mensagem solicitando uma nova partida, o sistema de reiniciar o jogo em caso de
# sim, e encerrar o programa em caso de não.
## Refatore a funcionalidade que verifica a vitoria e pense em uma forma de simplificar o código corrigido.

alunos = {}

def gerar_matricula():
    return str(len(alunos) + 1)

def cadastrar():
    print("\n--- Cadastro de Aluno ---")
    nome = input("Nome: ").strip()
    email = input("Email: ").strip()
    nascimento = input("Data de nascimento: ").strip()

    if nome == "" or email == "" or nascimento == "":
        print("Dados inválidos!")
        return

    matricula = gerar_matricula()

    alunos[matricula] = {
        "nome": nome,
        "email": email,
        "nascimento": nascimento
    }

    print(f"Aluno cadastrado com sucesso! Matrícula: {matricula}")

def atualizar():
    print("\n--- Atualizar Aluno ---")
    mat = input("Digite a matrícula: ")

    if mat in alunos:
        nome = input("Novo nome: ").strip()
        email = input("Novo email: ").strip()
        nascimento = input("Nova data de nascimento: ").strip()

        alunos[mat] = {
            "nome": nome,
            "email": email,
            "nascimento": nascimento
        }

        print("Aluno atualizado com sucesso!")
    else:
        print("Matrícula não encontrada!")

def remover():
    print("\n--- Remover Aluno ---")
    mat = input("Digite a matrícula: ")

    if mat in alunos:
        del alunos[mat]
        print("Aluno removido com sucesso!")
    else:
        print("Matrícula não encontrada!")

def listar():
    print("\n--- Lista de Alunos ---")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    for mat, dados in alunos.items():
        print("\nMatrícula:", mat)
        print("Nome:", dados["nome"])
        print("Email:", dados["email"])
        print("Nascimento:", dados["nascimento"])

def buscar():
    print("\n--- Buscar Aluno ---")
    mat = input("Digite a matrícula: ")

    if mat in alunos:
        dados = alunos[mat]
        print("\nMatrícula:", mat)
        print("Nome:", dados["nome"])
        print("Email:", dados["email"])
        print("Nascimento:", dados["nascimento"])
    else:
        print("Aluno não encontrado!")

# MENU
while True:
    print("\n===== SISTEMA DE ALUNOS =====")
    print("1 - Cadastrar aluno")
    print("2 - Atualizar aluno")
    print("3 - Remover aluno")
    print("4 - Listar alunos")
    print("5 - Buscar aluno")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        atualizar()
    elif opcao == "3":
        remover()
    elif opcao == "4":
        listar()
    elif opcao == "5":
        buscar()
    elif opcao == "0":
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida!")