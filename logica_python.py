# Criando variaveis

nome = 'Heverton'
sobrenome = 'Guimarães'
idade = 32
altura = 1.78
adulto = True

# Escrevendo no console.
print(nome)
print(sobrenome)
print(idade)
print(altura)
print(adulto)

# Concatetando informações
print('Meu nome é', nome, sobrenome)
print('Meu sobrenome é '+ sobrenome)
print('Minha idade é {} e minha altura é {}'.format(idade, altura))

# Maneira moderna(Bahiana) de concatenar
print(f'Meu nome é {nome} e tenho {idade} anos de idade')

# Verificação do tipo de variavel
print(type(nome))
print(type(sobrenome))
print(type(idade))
print(type(altura))
print(type(adulto))

# Expressões númericas

numero1 = 10
numero2 = 5

soma = numero1 + numero2
sub = numero1 - numero2
mult = numero1 * numero2
div = numero1 / numero2

print(F'A soma é {soma}')
print(F'A subtração é {sub}')
print(F'A multiplicação é {mult}')
print(F'A divivisão é {div}')

# Outras operações
expre = numero1 / (numero2 * numero2) + numero1
potencia = numero1**3
div_exata = numero1//4

print(f'A expressão é {expre}')
print(f'A potencia é {potencia}')
print(f'A divisão exata é {div_exata}')

