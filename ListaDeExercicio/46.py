## Desenvolva um programa que pergunte ao usuário para inserir 10 números e, ao final, exiba a média dos números inseridos.

soma = 0

for i in range(10):
    num = int(input("Digite um número: "))
    soma += num

media = soma / 10
print("Média:", media)