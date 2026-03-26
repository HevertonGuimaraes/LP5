## Crie uma nova versão do algoritmo 66, aplicando o conceito de módulos e dividindo as responsabilidades, receberemos agora não somente
# o nome, mas simularemos um sistema de cadastro de alunos, esta nova versão deve atender as novas funcionalidade a seguir:
## Cada aluno cadastrado deve ter atrelado a seus dados pessoais (nome, e-mail, data de nascimento, matricula), no caso de matricula você
# deve gerar uma matricula unica para cada aluno cadastrado.
## Cada um dos dados do aluno devem ser validade de forma o código não quebre ao serem informados valores incorretos.
## Para atualizar qualquer dado do aluno você deve localiza-lo utilizando de sua matricula para isso. Valide de forma que o sistema não
# quebre ao ser inserido uma matricula invalida.
## Para remover um aluno deve-se realizar esta ação usando de sua matricula, o sistema não pode quebrar ao ser inserido uma matricula
# errada.
## Ao listar todos os alunos mostre cada um de forma organizada e separada.
## Crie uma funcionalidade de mostre os dados de um aluno especifico usando apenas de sua matricula para isso.

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