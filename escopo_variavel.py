"""
Escopo de variavel
"""

# variável de escopo global
variavel = 'valor'


def func():
    print(variavel)


def func2(arg=None):
    arg = arg.replace('v', 'c')
    return arg


func()
print(func2(variavel))

print(variavel)
