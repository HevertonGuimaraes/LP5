## desenvolva um jogo da velha em python que funcione no terminal

tabuleiro = [" "] * 9

def mostrar_tabuleiro():
    print(f"""
 {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}
-----------
 {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}
-----------
 {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}
""")

def verificar_vitoria(jogador):
    combinacoes = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for c in combinacoes:
        if tabuleiro[c[0]] == tabuleiro[c[1]] == tabuleiro[c[2]] == jogador:
            return True

    return False

jogador = "X"

for rodada in range(9):
    mostrar_tabuleiro()

    try:
        pos = int(input(f"Jogador {jogador}, escolha posição (0-8): "))
    except:
        print("Digite um número válido!")
        continue

    if pos < 0 or pos > 8:
        print("Posição inválida!")
        continue

    if tabuleiro[pos] != " ":
        print("Posição já ocupada!")
        continue

    tabuleiro[pos] = jogador

    if verificar_vitoria(jogador):
        mostrar_tabuleiro()
        print(f"Jogador {jogador} venceu!")
        break

    # troca jogador
    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"

else:
    mostrar_tabuleiro()
    print("Deu empate!")