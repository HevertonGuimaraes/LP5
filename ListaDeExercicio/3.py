## Desenvolva um programa que pergunte ao usuário o dia da semana (número de 1 a 7) e exiba o nome do dia correspondente.

dia = int(input("Digite um número de 1 a 7: "))

if dia == 1:
    print("domingo")
elif dia == 2:
    print("segunda-feira")
elif dia == 3:
    print("terça-feira")
elif dia == 4:
    print("quarta-feira")
elif dia == 5:
    print("quinta-feira")
elif dia == 6:
    print("sexta-feira")
elif dia == 7:
    print("sábado")
else:
    print("Número inválido")