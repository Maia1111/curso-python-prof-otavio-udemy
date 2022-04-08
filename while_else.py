"""
While / Else

Contadores
Acumuladores

"""
# Contador
contador = 1
while contador <= 100:
    print(contador)
    contador = contador + 1

# Acumulador
contador = 1
acumulador = 1
while contador <= 10:
    print(contador, acumulador)
    acumulador = acumulador + contador
    contador += 1

print(acumulador)


# Na Linguagem Python o Laço While pode ter uma condicional else - Oque em outras linguagens não ocorre.
contador = 1

while contador <= 10:
    print(contador)
    contador += 1
else:
    print('Acabou!')
