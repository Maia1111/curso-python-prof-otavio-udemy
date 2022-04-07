"""
While em Python
utilizando para realizar ações enquanto uma condições é verdadeira

Requesitos: Ententder condições e separadores
"""
numero = 0

while numero <= 5:  # loop infinito
    print(numero)
    numero += 1

print('Acabou!')

# continue
# A palavra continue - continua o laço de repetição
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue
    print(x)
    x = x + 1

#  break
# break - para o laço de repetição

x = 9

while True:
    if x == 99:
        print(x)
        break
print(f'Achou o {x}')

