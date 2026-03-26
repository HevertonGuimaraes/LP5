## Escreva um programa que solicite ao usuário para inserir 3 nomes e armazene-os em uma lista. Em seguida, imprima a lista completa.

nomes = []

for i in range(3):
    nome = input("Digite um nome: ")
    nomes.append(nome)

print(nomes)