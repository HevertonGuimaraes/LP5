## Escreva um programa que peça ao usuário para escolher um modo de transporte (carro, bicicleta, a pé) e exiba uma mensagem com a velocidade média correspondente.

transporte = input("Escolha o transporte (carro, bicicleta, a pé): ")

if transporte == "carro":
    print("Velocidade média: 60 km/h")
elif transporte == "bicicleta":
    print("Velocidade média: 15 km/h")
elif transporte == "a pé":
    print("Velocidade média: 5 km/h")
else:
    print("Opção inválida")