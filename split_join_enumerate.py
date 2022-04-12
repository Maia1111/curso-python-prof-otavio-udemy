"""
Split, Join, Enumerate em Python

* split - Divide uma string # str
* Join - Junta uma lista # str
* Enumerate - Enumera elementos de lista # list
"""

string = 'O Brasil é o país do futebol, o Brasil é penta!'
lista_1 = string.split(' ')
lista_2 = string.split(',')
print(lista_1)
print(lista_2)

for valor in lista_1:
    print(f'A palavra "{valor}" apareceu {lista_1.count(valor)}X na frase')


print('========================================================================')

# Join serve pra juntar uma lista
# Ex:
string = 'O Brasil é penta.'
lista = string.split(' ')
string2 = ', '.join(lista)
print(string)
print(lista)
print(string2)

# Enumerate
for v1, v2, in enumerate(lista):
    print(f'indice: {v1} valor: {v2}')
