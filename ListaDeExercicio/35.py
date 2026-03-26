## Desenvolva um algoritmo que peça ao usuário para digitar dois números e verifique se a multiplicação deles é igual a 20.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 * n2 == 20:
    print("A multiplicação é igual a 20")
else:
    print("A multiplicação não é 20")