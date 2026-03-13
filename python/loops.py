# While laço de repetição quantidade indefinida a não ser que eu condicione a parada.

#cont = 0

#while True:
#    cont = cont + 1
#    print(cont)
#    if cont >= 100:
#        break

# sair = 'não'
# while sair != 'sim':
#     print('0 - Cadastrar')
#     print('1 - Editar')
#     print('2 - Excluir')

#     opcao = int(input('O que deseja realizar'))

#     match opcao:
#         case 0:
#             print('Você escolheu cadastrar')
#             sair = input('deseja sair sim ou não?')
#         case 1:
#             print('Você escolheu editar')
#             sair = input('deseja sair sim ou não?')
#         case 2:
#             print('Você escolheu excluir')
#             sair = input('deseja sair sim ou não?')
#         case _:
#             print('Opção inválida')
#             sair = input('deseja sair sim ou não?')

# For Repertição pre definida de vezes.

# for numero in range(1, 10):
#     print(numero)

# percorrendo listas de forma indivizualizada

# frutas  = ['Uva', 'Maça', 'Abacaxi', 'Kiwi', 'Gabriel']
# for  fruta in frutas:
#     if fruta == 'Gabriel':
#         print('Comi e não gostei!')

nome = 'Gabriel'

for letra in nome:
    print(letra)