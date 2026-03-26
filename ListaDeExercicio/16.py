## Desenvolva um programa que peça ao usuário um tipo de combustível (gasolina, etanol, diesel) e exiba o preço correspondente por litro.

combustivel = input("Digite o tipo de combustível: ")

if combustivel == "gasolina":
    print("Preço: R$ 6.50 por litro")
elif combustivel == "etanol":
    print("Preço: R$ 3.80 por litro")
elif combustivel == "diesel":
    print("Preço: R$ 6.00 por litro")
else:
    print("Combustível inválido")