"""
Operador Ternario

"""

logged_user = True

msg = 'Usuário Logado!' if logged_user else 'Usuário precisa logar'
print(msg)

idade = input()
msg2 = 'Pode acessar' if idade >= 18 else 'Não pode acessar'

print(msg2)
