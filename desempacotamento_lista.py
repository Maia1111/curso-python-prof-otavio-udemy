"""
Desempacotamento de lista em Python

"""
lista = ['Luiz', 'João', 'Maria']
n1, n2, n3 = lista
print(n2)


# Desempacotamento quando a lista é extensa
lista2 = [1, 2, 3, 4, 5, 6, 8]


# Desempacotar parte da lista em variáveis e outra parte em uma lista
# Se o numero de variáveis no desempacotamento for menor que numero de elementos na lista
# Gera um erro
n4, n5, n6, *outra_lista = lista2
print(n4, n5, n6, outra_lista)
