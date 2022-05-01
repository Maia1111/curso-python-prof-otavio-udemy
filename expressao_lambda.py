"""
Expressão Lambda ( função


"""

a = lambda x, y: x * y

print(a(2, 2))

# Quando vc utiliza expressão Lambda
# normalmente quando vc precisa passar uma expressão como parâmetro pra outras funções


lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8]
]

# Ordenando do menor pro maior
lista.sort(key=lambda item: item[1])
print(lista)

# Odernando do maior pro menor ( sort altera a lista)
lista.sort(key=lambda item: item[1], reverse=True)
print(lista[:-1])

# outra maneira de ordenar a lista utilizando sorted,  não altera a lista original
print(sorted(lista, key=lambda i: i[1]))

# A diferença do sort para o serted é que o sort altera a lista original e o sorted não.
