## Desenvolva um algoritmo que solicite ao usuário uma senha e continue pedindo até que a senha correta "1234" seja digitada.


senha = ""

while senha != "1234":
    senha = input("Digite a senha: ")

print("Acesso liberado")