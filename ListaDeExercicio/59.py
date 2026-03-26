## Escreva um programa que solicite ao usuário para digitar dois números e verifique se o primeiro é maior que o segundo. Continue pedindo números até que o primeiro número seja maior que o segundo.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

while n1 <= n2:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

print("Agora o primeiro é maior")