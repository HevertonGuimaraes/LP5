### Escreva um algoritmo que forneça um menu para o usuário: 1-Cadastrar nome, 2- atualizar o nome, 3, excluir, 4-listar todos os 
### cadastrados, ao final da operação deve dar uma mensagem indicando o resultado da operação e perguntando se deseja realizar
### outra operação, o seu aplicativo apenas deve encerrar quando a opção não for inserida.

cadastros = []

while True:
    print("\n1 - Cadastrar nome")
    print("2 - Atualizar nome")
    print("3 - Excluir nome")
    print("4 - Listar nomes")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ").strip()
        cadastros.append(nome)
        print("Nome cadastrado com sucesso!")

    elif opcao == "2":
        if len(cadastros) == 0:
            print("Lista vazia!")
        else:
            nome = input("Digite o nome que deseja atualizar: ").strip()

            if nome in cadastros:
                novo = input("Digite o novo nome: ").strip()
                indice = cadastros.index(nome)
                cadastros[indice] = novo
                print("Nome atualizado!")
            else:
                print("Nome não encontrado!")

    elif opcao == "3":
        if len(cadastros) == 0:
            print("Lista vazia!")
        else:
            nome = input("Digite o nome para excluir: ").strip()

            if nome in cadastros:
                cadastros.remove(nome)
                print("Nome removido!")
            else:
                print("Nome não encontrado!")

    elif opcao == "4":
        if len(cadastros) == 0:
            print("Nenhum nome cadastrado.")
        else:
            print("\nLista de nomes:")
            for n in cadastros:
                print("-", n)

    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")