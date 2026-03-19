def soma (numero1, numero2):
    """
        Esta função recebe dois numeros inteiros e realiza a soma do mesmos.
    """

    soma = numero1 + numero2
    print(f'O resultado da sua soma é:{soma}')


def sub (numero1, numero2):
    """
        Esta função recebe dois numeros inteiros e realiza a subtracao do mesmos.
    """
    sub = numero1 - numero2
    print(f'O resultado da sua subtração é:{sub}')

def menu():
    print('1 - Somar')
    print('2 - Subtrair')
    opcao = input ('2 - O que deseja realiza?')
    return opcao