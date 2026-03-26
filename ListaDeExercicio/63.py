## Desenvolva um algoritmo que peça ao usuário para inserir 5 números, adicione-os a uma lista e, depois, exiba a soma de todos os números na lista.

lista = []

for i in range(5):
    num = int(input("Digite um número: "))
    lista.append(num)

print("Soma:", sum(lista))