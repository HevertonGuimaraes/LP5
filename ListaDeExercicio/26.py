## Desenvolva um algoritmo que peça ao usuário para inserir dois números e verifique se ambos são múltiplos de 5.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 % 5 == 0 and n2 % 5 == 0:
    print("Ambos são múltiplos de 5")
else:
    print("Nem todos são múltiplos de 5")