# Desafio
"""
Criar variável para nome (str), idade(int),
altura (float), e peso (float), ano atual (int)
Obter o ano de nascimento da pessoa ( baseado na idade e no ano atual)
Obter o IMC da pessoa com duas casas decimais
Exibir um texto com todos os valores na tela utilizando  F-strings (chaves)
"""

# Resolução do desafio
nome = 'Rogério'
altura = 1.89
peso = 100.0
idade = 41
ano_atual = 2022
ano_nascimento = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso:.0f}Kg.'
      f'\nO IMC é {imc:.2f}.'
      f'\n{nome} nasceu em {ano_nascimento}.')




