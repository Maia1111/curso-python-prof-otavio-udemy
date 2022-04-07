# Exercicio 1
numero = input('digite um numero: ')
if numero.isnumeric():
    numero = int(numero)
    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é ímpar')
else:
    print('Você precisa digitar um numero inteiro')


# Exercicio 2
hora = input("Digite uma horario entre 0 - 23: ")
if hora.isnumeric():
    hora = int(hora)
    if hora > 23:
        print('Você digitou uma hora inválida.')
    elif hora <= 11:
        print('Bom dia')
    elif hora <= 17:
        print('Boa tarde')
    else:
        print('Boa noite')
else:
    print("voce digitou uma hora invalida!")

# Exercicio 3
nome = input("Digite seu nome: ")
if len(nome) >= 5 or len(nome) <= 6:
    print('Seu nome é normal')
elif len(nome) > 6:
    print('Seu nome é muito grande')
else:
    print('Seu nome é muito curto')
