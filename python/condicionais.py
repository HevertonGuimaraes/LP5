# condicional if com operadores relacionais <, >, >=, <=, ><, ==

# idade = 18
# acompanhada = 'Sim'


# if idade < 0:
#     print("Idade inválida")
# elif idade < 15:
#     print("Entrada não permitida para menores de idade")
# elif idade <= 17:
#     if acompanhada.lower() == 'sim':
#         print("Você pode assistir o filme")
#     else:
#         print("Você não pode assistir o filme")
# else:
#     print("Entrada permitida")

# Operadores Lógicos and, or, not

# if idade >= 18:
#     print("Entrada permitida")
# elif idade >=15 and idade<= 17:
#     if acompanhada.lower() == 'sim':
#         print("Você pode assistir o filme")
#     else:
#         print("Você não pode assistir o filme")
# else:
#     print("Entrada permitida")

print('0 - Cadastrar')
print('1 - Editar')
print('2 - Excluir')

opcao = int(input('O que deseja realizar'))

match opcao:
    case 0:
        print('Você escolheu cadastrar')
    case 1:
        print('Você escolheu editar')
    case 2:
        print('Você escolheu excluir')
    case _:
        print('Opção inválida')