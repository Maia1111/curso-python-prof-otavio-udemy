"""
Funções parte 2 (def) em Python - return

Quando vc não coloca a palavra reservado return em uma função Python
Ela retorna None
"""


def funcao(var):
    return var


variavel = funcao('Valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum valor')


def divisao(n1, n2):
    if n2 > 0:
        return n1 / n2
    else:
        return 'Conta invalida, não se pode dividir um número por zero.'


divide = divisao(8, 3)
print(f'{divide:.2f}')
