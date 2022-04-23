"""
Funções (def) em Python - *args **Kwargs

Aula funções parte 3

"""


def func(a1, a2, a3, a4, a5,):
    return print(a1, a2, a3, a4, a5)


func(1, 2, 3, 4, 5)


# Refatorando utilizando os args
def func2(*args):
    print(args)


func2(1, 2, 4, 'Rogério')

# Desempacotando uma lista no print
lista = [1, 2, 3, 4, 5]
print(*lista, sep='-')


def func2(*args, **kwargs):
    print(args)
    print(kwargs)


lista = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9]

# Passandop um lista com asterisco pra desempacotar e passando tambeém argumentos nomeados
func2(*lista, *lista2, nome='Rogério', sobrenome='Maia')

