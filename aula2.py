# a
print('Luiz', 'Otávio', sep='-')
print('João', 'e' 'Otávio')

'''
Criar uma mascara para numero de CPF exercício
'''

numero = input("Digite seu CPF: ")
print(numero[0:3], numero[3:6], numero[6:9], sep='.', end='')
print(f'-{numero[9:11]}')
