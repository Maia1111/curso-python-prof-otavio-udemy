
usuario = input('Digite seu usuário: ')
qtd_caractere = len(usuario)

if qtd_caractere < 6:
    print('Você precisa digitar pelo menos 6 caracteres')
else:
    print('Você foi cadastrado no sistema.')

string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa:')

print(f'A quantidade de caractere digitados foi {len(string1+string2)}')


# floot não tem len
# boleanos também não tem len
