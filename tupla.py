"""
A diferença entre tupla e lista é que a tupla é imutavel: você não pode
retirar nem adicionar item.

A forma de acesso e iteração é a mesma das listas

a Tupla pode ser criada sem utilização dos parênteses

Oque define uma tupla é a virgula e não o parênteses

"""

t1 = (1, 2, 3, 'a', 'Luiz otavio')
print(t1)

# acessando pelo indice
print(t1[0])

# Acessando do indice 0 ao ultimo índece
print(t1[0:-1])

# Acessando do índece 2 ao ultimo indece
print(t1[2:-1])


print(t1[len(t1):0:-1])
