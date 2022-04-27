
"""
1 - Crie uma função1 que recebe uma função dois como barametro e retorna o valor da função dois executada

"""


# Resolução do 1
def func1():
    return 'Ola Mundo!'


def func2(funcao):
    return funcao()


executando = func2(func1)
print(executando)


# Resolução 2
def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_io(nome):
    return f'Oi {nome}'


def saudacao(nome, cumprimento):
    return f'{cumprimento} {nome}'


executando = mestre(fala_io, "Luiz")
executando2 = mestre(saudacao, 'Luiz', 'tudo bem')


print(executando)
print(executando2)


