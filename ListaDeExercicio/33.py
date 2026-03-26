## Crie um programa que solicite ao usuário o valor de um produto e calcule o desconto de 10%.

valor = float(input("Digite o valor do produto: "))

desconto = valor * 0.10
novo_valor = valor - desconto

print("Valor com desconto:", novo_valor)