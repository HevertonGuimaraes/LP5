## Escreva um programa que pergunte ao usuário quantas vezes ele quer que uma mensagem seja exibida, e utilize um laço while para exibir a mensagem a quantidade de vezes desejada.

vezes = int(input("Quantas vezes deseja repetir? "))

contador = 0

while contador < vezes:
    print("Mensagem")
    contador += 1