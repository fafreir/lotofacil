import random
import os

# Gerando os 15 numeros
lista = list()
for i in range(1, 16):
    sorteio = random.choices(range(1, 26))
    if sorteio not in lista:
        lista.append(sorteio)
    else:
        while sorteio in lista:
            sorteio = random.choices(range(1, 26))
        else:
            lista.append(sorteio)


def formatacao(lista):
    return str(lista).replace('[', '').replace(']', '')


# Conversão para inteiro
try:
    number = list()
    for i in range(0, 16):
        word = str(sorted(lista[i])).replace('[', '').replace(']', '')
        a = int(word)
        number.append(a)
except IndexError:
    pass

ordenacao = formatacao(sorted(number))

print(f'Os numeros sorteados são: {os.linesep} {(ordenacao)}')
