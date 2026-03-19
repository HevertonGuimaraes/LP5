# nome = 'Luciano'
# print(f'Meu nome é: {nome}')

# nome = 'Marcelo'
# print(f'Meu nome é: {nome}')

# nomes = ['Luciano', 'Marcelo']
# print(nomes[0])
# print(nomes[1])

## Percorrendo a lista posição por posição
apostolos = ['Matheus', 'Thiago', 'Lucas', 'Judas', 'Pedro']

# for apostolo in apostolos:
#     print(apostolo)

## adicionando item no final da lista
# apostolos.append('João')
# print(apostolos)

##Adicionando item na posição desejada
# apostolos.insert(2,'Simão')
# print(apostolos)

## Expandindo a lista com novos elementos
cavaleiros = ['Seiya', 'Shiriu']
print(cavaleiros)

cavaleiros.extend(['Ikki', 'Yoga', 'Shun'])
print(cavaleiros)

# excluindo itens da lista
cavaleiros.pop()
print(cavaleiros)

cavaleiros.pop(0)
print(cavaleiros)

## excluindo por valor
# print(apostolos)
# apostolos.remove('Judas')
# print(apostolos)

alunos = ['Victor', 'Lucas', 'Gabriela', 'Lucas', 'Amanda', 'Daniel']
print(alunos)

# alunos.remove('Lucas')
# print(alunos)

for indice, aluno in enumerate(alunos):
    if aluno == 'Lucas':
        alunos.pop(indice)
print(alunos)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impares = []
pares = []

for indice, numero in enumerate(numeros):
    if numero % 2 != 0:
        impares.append(numero)
    elif numero % 2 == 0:
        pares.append(numero)

print(impares)
print(pares)

print(apostolos)
apostolos.sort() ## ordena do primeiro ao ultimo
print(apostolos)
apostolos.reverse() ##ordena do ultimo ao primeiro
print(apostolos)

print(cavaleiros)
cavaleiros.clear() ##zera lista
print(cavaleiros)

print(pares)
del pares ## apaga de forma definitiva
print(pares)

