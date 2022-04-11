secreto = 'Perfume'
secreto_temporario = ''
digitadas = []

for n in secreto:
    letra = input('Digite uma letra: ')
    digitadas.append(letra)

for letra_secreta in secreto:
    if letra_secreta in digitadas:
        secreto_temporario += letra_secreta
    else:
        secreto_temporario += '*'

print(f"A sua dica de palavra é'{secreto_temporario}'")
secreto_temporario = input('Qual é a palavra ? ')
secreto_temporario = secreto_temporario.strip()


if secreto_temporario == secreto:
    print(f"Você acertou, a palavra secreta é '{secreto}'.")

else:
    print('Não foi dessa vez, você náo acertou a palavra secreta.')



