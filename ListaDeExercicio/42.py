## Escreva um algoritmo que solicite ao usuário 5 números inteiros e calcule a soma desses números.

soma = 0

for i in range(5):
    num = int(input("Digite um número: "))
    soma += num

print("Soma:", soma)