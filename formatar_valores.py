"""
Formatando valores com modificados

:s - Texto ( strings)
:d - Inteiro (int)
:f  Para indicar que é um numero de ponto fluatuante
:. Quantidade de casas decimais (float)
: ( caracteres)  (> ou < ^ ) ( quantidade) ( Tipo - s, d ou f )

> - Direita
< Esquerda
^ Centro


"""

num_1 = 10
num2 = 3
divisao = num_1 / num2
num3 = 1


print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')
print(f'{num3:0>10}')
print(f'{num3:.2f}')
print(f'{num3:0>10.2f}')

nome = 'Rogério Maia'
nome_formatado = '{:#^50}'.format(nome)
print(nome_formatado)

print(nome.lower())  # Tudo monúsculas
print(nome.upper())  # tudo Maiusculas
print(nome.title())  # Primeira Letra maiúsculas

