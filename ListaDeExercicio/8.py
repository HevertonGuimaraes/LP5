## Desenvolva um algoritmo que pergunte ao usuário o estado civil (solteiro, casado, divorciado, viúvo) e exiba uma mensagem correspondente.

estado = input("Digite seu estado civil: ")

if estado == "solteiro":
    print("Você é solteiro(a).")
elif estado == "casado":
    print("Você é casado(a).")
elif estado == "divorciado":
    print("Você é divorciado(a).")
elif estado == "viúvo":
    print("Você é viúvo(a).")
else:
    print("Estado civil inválido.")