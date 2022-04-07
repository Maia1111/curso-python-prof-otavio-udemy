"""
Manipulando Strings

* String Indices
* Fatiamento de Strings [Inicio:Fim:passo]
* Funções built-in len, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo

Voçê pode conferir tudo  iso em:
https://docs.python.org/3/library/stdtype.html   (tipos built-in)
https://docs.python.org/3/library/functions.html

"""

# indices
# Positivos        012345678
texto =           'Python s2'
# Negativos        876543210

url = 'www.google.com.br/'
print(url[:-1])  # Imprimindo retirando o ultimo caractere

nova_string = texto[2:6]
print(nova_string)
print(texto[0:-1])

nova_string = texto[0:6:2]  # inicio:fim:passo
print(nova_string)
print(len(nova_string))

nova = texto.replace('P', 'v')
print(nova)
