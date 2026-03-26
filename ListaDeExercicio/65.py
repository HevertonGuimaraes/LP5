## Escreva um programa que solicite ao usuário uma lista de 5 números e exiba o maior e o menor número dessa lista.

lista = []

for i in range(5):
    num = int(input("Digite um número: "))
    lista.append(num)

print("Maior:", max(lista))
print("Menor:", min(lista))