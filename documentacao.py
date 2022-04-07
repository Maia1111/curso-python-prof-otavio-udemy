num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')


if num1.isnumeric() and num2.isnumeric():
    print(f'Resultado da soma é : {int(num1)+ int(num2)}')
else:
    print('Você precisa digitar somente números.')

