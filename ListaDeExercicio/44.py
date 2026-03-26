## Crie um programa que peça ao usuário 10 números e exiba apenas os números pares.

for i in range(10):
    num = int(input("Digite um número: "))
    
    if num % 2 == 0:
        print("Par:", num)