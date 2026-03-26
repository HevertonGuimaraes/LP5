## Faça um programa que peça ao usuário três números e verifique se todos são positivos.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 > 0 and n2 > 0 and n3 > 0:
    print("Todos são positivos")
else:
    print("Nem todos são positivos")