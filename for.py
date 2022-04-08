
"""
for in Python

Iterar  em estrutar iteráveis

função range (inicio, parada, passo)

"""

texto = 'python'
# for simples
for letra in texto:
    print(letra)

# Colocando um enumarate no for, enumerate enumera a quantidade de laços de repetição
for n, letra in enumerate(texto):
    print(n, letra)

# função range recebe 3 parametros (inicio, fim, passo)
# quando não indicamos o parametro ela coloca o parametro padrão
for numero in range(0, 10, 2):
    print(numero)

# range ao contrario

for num in range(20, 0, -1):
    print(num)

for n in range(101):
    if n % 2 == 0:
        print(n)

# pulando a letra p do texto da string
for letra in texto:
    if letra == 'p':
        continue
    print(letra)

