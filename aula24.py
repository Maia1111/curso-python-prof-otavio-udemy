"""
Operadores Relacionais

Operadores de comparação
== igual
>  Maior que
>= Maior que ou igual a
<  Menor que
<= Menor que ou igual a
!= Diferente
"""
num1 = 2
num2 = 2

expressao = num1 == num2
print(expressao)
print(num1 > num2)

nome = input('Qual o seu nome? ')
idade = input('Qual sua idade? ')
idade = int(idade)
idade_menor = 20
idade_maior = 30


if idade > idade_menor and  idade <= idade_maior:
    print(f'{nome} pode pegar empréstimos.')
else:
    print(f'{nome} NÃO pode pegar empréstimos.')




