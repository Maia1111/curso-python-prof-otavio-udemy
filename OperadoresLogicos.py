"""
Operadores lógicos
and, or, not
in  e not in

"""

nome = 'vio'


if 'vio' not in nome:
    print('Executei')
else:
    print(f'Existe ')

# Simulando um entrada com login e senha
usuario = input('Nome usuário: ')
senha = input('Senha usuário: ')

usuario_bd = 'rogerio'
senha_db = '123456'

if usuario == usuario_bd and senha == senha_db:
    print("Você esta logado no sistema")
else:
    print('Você digitou uma senha ou usuário inválidos!')
