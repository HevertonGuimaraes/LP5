## Crie um programa que peça ao usuário para inserir números até que ele digite o número 0. Ao final, exiba a soma de todos os números inseridos (exceto o 0).

soma = 0

while True:
    num = int(input("Digite um número (0 para parar): "))
    
    if num == 0:
        break
    
    soma += num

print("Soma:", soma)