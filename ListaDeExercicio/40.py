## Escreva um programa que peça ao usuário para inserir três números e verifique se todos são iguais.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 == n2 and n2 == n3:
    print("Todos são iguais")
else:
    print("Nem todos são iguais")