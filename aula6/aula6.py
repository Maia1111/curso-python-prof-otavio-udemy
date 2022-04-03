"""
Iniciar com letra, pode conter numeros, separar _, letras minusculas

"""
nome = "Rogério"
idade = 40  # int
altura = 1.89  # float
e_maior = idade > 18  # int
data_atual = 2022  # int
data_1 = False  # bool
peso = 100.0
imc = peso / (altura ** 2)

print('Nome: ', nome)
print('Idade: ', idade)
print('Altura: ', altura)
print('É maior de idade: ', e_maior)
print(idade * altura)

# print  utilizando o f de format
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')

# print utilizando a função format no final
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))

# print utilizando  ordendo o recebimento dos parêmetros
print('{0} tem {1} anos de idade e seu imc é {2}'.format(nome, idade, imc))

# print com parâmetros nomeados
print('{n} tem {i} anos de idade e seu imc é {m} '.format(n=nome, i=idade, m=imc))
