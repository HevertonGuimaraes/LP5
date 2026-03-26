## Crie um algoritmo que solicite ao usuário um número e continue pedindo outro número até que um número negativo seja inserido.

while True:
    num = int(input("Digite um número: "))
    
    if num < 0:
        break