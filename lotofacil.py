# Gerador Lotofácil
from random import randint

x = 0
lista = []

while x <= 14:
    sorteado = randint(1, 25)
    if sorteado not in lista:
        lista.append(sorteado)
    else:
        x = x - 1
    x += 1

lista.sort()
print(f'Gerador Lotofácil: {str(lista)[1:-1]}')
