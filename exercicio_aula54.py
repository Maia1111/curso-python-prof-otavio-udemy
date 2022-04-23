
"""
Exercícios propostos aula 54
"""


"""
1 - Crie uma função que exiba uma saudação com os parâmetros saudação e nome.
"""


# Resolução exercicio 1
def saudacao(msg, nome):
    return f'{msg} {nome}.'


cumprimento = saudacao('Olá, tudo bem', 'Rogério')
print(cumprimento)


"""
2 - Cria uma função que receba 3 números com parâmetros e return as somas entre eles
"""


# Resolução do exercício 2
def soma(*args):
    return sum(args)


conta = soma(1, 2, 3, 4)
print(conta)

"""
3 - Crie uma função que receba dois numeros. O primeiro é um valor e segundo é um percentual 
(ex: 10%) . Retorne o valor do primeiro somado aumento com o percentual do segundo parâmetro
"""


# Resolução do exercício 3
def aumento_percentual(numero, percentual):
    percentual = percentual / 100
    aumento = numero * percentual
    resultado = numero + aumento
    return resultado


soma_percentual = aumento_percentual(250, 50)
print(soma_percentual)


"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz, se o parâmetro 
da função for divisível por 5, retorne buzz. Se o parâmetro da funcão for divisível por 5 e por 3, 
retorne FizzBuzz
"""


# Resolução do exercício 4
def fiiz_buzz(numero):
    if numero % 5 == 0 and numero % 3 == 0:
        return f'FizzBuzz, {numero} é divisível por 3 e 5.'
    if numero % 3 == 0:
        return f'fizz, {numero} é divisível por 3'
    if numero % 5 == 0:
        return f'buzz, {numero} é divisível por 5'
    return f'{numero}, não é divisível nem por 3 nem por 5.'


print(fiiz_buzz(9))   # somente dividido por 3
print(fiiz_buzz(25))  # somente dividido por 5
print(fiiz_buzz(15))  # dividido por 5 e por 3
print(fiiz_buzz(31))  # Não divisível nem por 3 nem por 5
