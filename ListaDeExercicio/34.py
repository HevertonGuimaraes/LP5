## Escreva um programa que peça ao usuário um número e verifique se ele é positivo, negativo ou zero.

numero = int(input("Digite um número: "))

if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Zero")