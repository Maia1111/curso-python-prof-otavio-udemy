"""
Operador  condicinal OR

"""

nome = input('Qual o seu nome? ')

if nome:
    print(nome)
else:
    print('você não digitou nada =( ')

# Simplificando o codigo acima com or
print(nome or 'Você não digitou nada =(')


# Armazenar valores True em uma variável
a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Luiz'

# A primeira variável True que ele achar vai armazenar
variavel = a or b or c or d or e or f or g
print(variavel)
