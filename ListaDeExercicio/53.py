## Escreva um programa que peça ao usuário um número e exiba a contagem regressiva desse número até 1.

num = int(input("Digite um número: "))

for i in range(num, 0, -1):
    print(i)