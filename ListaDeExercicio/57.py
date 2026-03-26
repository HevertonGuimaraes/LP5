## Crie um programa que peça ao usuário para adivinhar um número secreto entre 1 e 10. Continue pedindo até que ele adivinhe o número corretamente.

numero_secreto = 7

num = int(input("Adivinhe o número (1 a 10): "))

while num != numero_secreto:
    num = int(input("Tente novamente: "))

print("Acertou!")