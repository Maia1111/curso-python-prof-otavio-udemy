"""
Dicionarios
No dicionario é uma estrura de dados com chave e valor

Em dicionarios vc pode utilizar qualquer tipo de dados imutável.

Normalmente se utiliza strings como chaves, mais vc pode numeros, e
outros tipos de dados em Python.

O dicionário não aceita chaves duplicadas, caso tenha, ele vai
considerar a ultima chave

"""
# Forma 1 de atribuir um dicionário
d1 = {'chave': 'valor da nova chave'}
print(d1)

# Outra forma de criar dicionário
d2 = dict(chave1='Valor da chave1')
print(d2['chave1'])


# chaves podem ser qualquer estrutura de dados imutável
d3 = {
    'chave1': 'valor',
    'chave2': 'outro valor',
    'chave3': 'Tupla'
}

# Quando tentamos acessar uma chave que não existe o código gera uma exeção.
# print(d1['Não existe'])

print(d1.get('nomedachave'))

# Formas de atualizar um dicionário

# Forma 1
d3.update({'chave1': 'novo_valor'})

# Checando se a chave não é None
if d3.get('chave1') is not None:
    print(d3['chave1'])

print(d3)

# Apagando uma chave de um dicionario
print('\nTem um código acima que deleta a chave1 do dicionário d3')
del d3['chave1']

# mostrando apos ter apagado a chave 'str'
print(d3)

# checando chaves e valores de um dicionário
print('valor' in d1.keys())  # checando se existe a chave 'valor' no dicionário
print('novo_valor' in d3.values())  # checando se existe o 'novo_valor' no dicionário


# Checando quanto par de chaves valor existe no meu dicionário
print(len(d3))

# iterando sobre um dicionário

# Iterando e mostrando as  chaves e valores do dicionario d3
print('\nMostrando chave e valores do dicionário d3')
for i in d3.items():
    print(i)

# Iterando e mostrando  somente as chave do dicionário d3
print('\nMostrando somente as chaves dicionário d3')
for i in d3.keys():
    print(i)

# Iterando e mostrando  somente os valores do dicionário
print('\nMostrando somente os valores do dicionário')
for i in d3.values():
    print(i)

d1['chave'] = 'mudei o valor da chave'
print(d1.get('chave'))


clientes = {
     'cliente1': {
         'nome': 'Luiz',
         'sobrenome': 'Otávio'
     },
     'cliente2': {
         'nome': 'João',
         'sobrenome': 'Moreira'
       },
     'cliente3': {
         'nome': 'Maria',
         'sobrenome': 'da Silva'
       }
}


for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} {dados_v}')
    print('=============================================')

# Apagando itens do dicionários com  função pop
# para apagar com função pop você precisa passar a chave que será deletada
# Para apagar sem passar chave você deve utilizar popitem, ai apaga sempre ultimo item do dicionário

d1 = {
    1: 2,
    2: 3,
    4: 5
}
# mostrando o dicionário com todos os itens
print(d1)

# Apagando o item da chave 1
d1.pop(1)
print(d1)

# Apagando o ultimo item utilizando popitem
d1.popitem()
print(d1)


# Unindo um dicionario a outro utilizando a função update

dic1 = {'a': 1, 'b': 2, 'c': 3}
dic2 = {'d': 4, 'e': 5, 'f': 6}

print(dic1)
print(dic2)

# Unindo os dois dicionários
dic1.update(dic2)
print(dic1)
