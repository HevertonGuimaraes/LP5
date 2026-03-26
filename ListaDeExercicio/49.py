## Desenvolva um programa que peça ao usuário para inserir 7 números e, ao final, exiba quantos desses números são maiores que 10.

contador = 0

for i in range(7):
    num = int(input("Digite um número: "))
    
    if num > 10:
        contador += 1

print("Quantidade maior que 10:", contador)