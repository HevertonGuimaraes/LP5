## Desenvolva um algoritmo que peça ao usuário para digitar dois números e verifique se a soma deles é maior que 100.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

soma = n1 + n2

if soma > 100:
    print("A soma é maior que 100")
else:
    print("A soma não é maior que 100")