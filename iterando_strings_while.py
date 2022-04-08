
"""
# Iterando strings com while
#
# """

frase = 'O rato roeu a roupa do rei de roma'
tamanho_da_frase = len(frase)
contador = 0

# while contador < tamanho_da_frase:
#     print(frase[contador], ' índice:', contador)
#     contador += 1

# Montando string em outra strings

nova_string = ""
# contador = 0
while contador < tamanho_da_frase:
    nova_string += frase[contador]
    contador += 1
    print(nova_string)


contador = 0

frase_nova = ''

while contador < tamanho_da_frase:
    letra = frase[contador]
    if letra == 'r':
        frase_nova += 'R'
    else:
        frase_nova += letra
    print(frase_nova)
    contador += 1
