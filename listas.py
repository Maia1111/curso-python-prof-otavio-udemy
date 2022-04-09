"""
Listas em Python
fatiamento

append, insert, pop, del, clear, extend, +
min, max.
range

"""
# índece  0      1       2    3    4    5
lista = ['A', 'Bacana', 'C', 'D', 'E', 10.5]

# Acessando o índice 1 da lista
print(lista[1])
print(lista[5])

# se eu quizer mudar qualquer um dos índice
lista[5] = 'Qualquer coisa'
print(lista[5])
print(lista[::2])

# invertendo a lista
print(lista[::-1])

# unindo listas
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l1)
print(l2)

# Adicionou a l2 a l1, mais não com itens individuais e sim a lista inteira
l1.append(l2)
print(l1)

# extendendo uma lista para outra
l3 = [1, 2, 3]
l4 = [4, 5, 6]
l3.extend(l4)
print(l3)

# Unindo duas listas com sinal de +
l5 = [1, 2, 3]
l6 = [4, 5, 6]
l7 = l5 + l6
print(l7)

# A função append vai adicinar um elemento no final da lista
l5.append('b')
print(l5)

# A função insert inseri um elemento na lista onde vc escollher
# A função tem dois parâmetros, o primeiro o indice que vc quer inserir e o segundo o elemento
# exemplo ->    l5.insert(0, 'banana')
l5.insert(0, 'Banana')
print(l5)

# Removendo um elemento da lista
# a função pop remove do final da lista ou você pode especificar o indice
l5.pop()
l5.pop(0)
print(l5)

# Deletando de uma lista utilizando o del
l2 = [1, 2, 3, 4, 5, 6]
print(f'Lista2 antes de excluir {l2}')
del(l2[0:3])
print(l2)

# Mostrando os maximos e mínimos com as funções max e min
print(max(l2))
print(min(l2))

# Criando uma lista com range
# Quando vc cria objeto range ele não cria de imediato uma lista, é preciso converter
# utilizando list
l8 = range(0, 10)
print(list(l8))

# Uma forma mais verbosa de criar uma lista de numeros e iterar sob ela
l9 = list(range(0, 100, 2))
for num in l9:
    print(num)

l10 = [0, 1, 2, 3, 4, 5, 6, 7]
soma = 0
for valor in l10:
    soma += valor
print(soma)
print(sum(l10))
