## Faça um programa que pergunte ao usuário a idade e verifique se ele pode votar (idade maior ou igual a 16).

idade = int(input("Digite sua idade: "))

if idade >= 16:
    print("Pode votar")
else:
    print("Não pode votar")