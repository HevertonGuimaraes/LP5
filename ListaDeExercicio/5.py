## Faça um programa que solicite ao usuário dois números e verifique se ambos são pares.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Ambos os números são pares")
elif num1 % 2 == 0 and num2 % 2 != 0:
    print("O primeiro número é par e o segundo é ímpar")
elif num1 % 2 != 0 and num2 % 2 == 0:
    print("O primeiro número é ímpar e o segundo é par")
else:
    print("Ambos os números são ímpares")