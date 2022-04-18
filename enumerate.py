"""
Enumerate - Enumerar elementos em uma lista # list

"""

lista = [
    ['Edu', 'João', 'Luiz'],
    ['Maria', 'Aline', 'Joana'],
    ['Helena', 'Edu', 'Lu']
]

enumerada = enumerate(lista)
print(enumerada)


enumerada = list(enumerada)  # Cast do objeto enumate para list
print(enumerada)

# for em enumerate de lista
for n1, n2 in enumerate(lista):
    print(n1, n2)


# Enumerate Não serve  exatamente pra controlar indice e sim pra enumerar
# Você pode mudar o início do enumerate passando um parametro de início
# Por padrão ele inicia em 0"
for n1, n2 in enumerate(lista, 53):
    print(n1, n2)

