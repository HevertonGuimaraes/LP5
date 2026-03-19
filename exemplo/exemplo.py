import os
from funcoes import soma, sub, menu

continuar = 's'
while continuar != 'n':
    os.system('cls')
    opcao = menu()
    
    numero1 = int(input("Informe o primeiro numero:"))
    numero2 = int(input("Informe o segundo numero:"))

    if opcao == '1':
        soma(numero1, numero2)
    elif opcao == '2':
        sub(numero1, numero2)
    else:
        print('Opção inválida.')
    continuar = input('Deseja realizar outra operaçao s/n ')