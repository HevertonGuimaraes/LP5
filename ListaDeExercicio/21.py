## Escreva um algoritmo que peça ao usuário para digitar um número e verifique se ele é maior, menor ou igual a 10.

numero = int(input("Digite um número: "))

if numero > 10:
    print("Maior que 10")
elif numero < 10:
    print("Menor que 10")
else:
    print("Igual a 10")