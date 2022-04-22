"""
Desafio contadores

"""

cont1 = 0
cont2 = 10

for n in range(9):
    print(f'{cont1} {cont2}')
    cont1 += 1
    cont2 -= 1

print('=============================================')

# Resolução com enumerate
for p, r in enumerate(range(10, 1, -1)):
    print(f'{p}, {r}')
