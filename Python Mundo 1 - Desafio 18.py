#Desafio catetos

from math import sqrt, pow, hypot

catetoOposto = float(input('Digite o comprimento do cateto oposto'))
catetoAdjacente = float(input('Digite o comprimento do cateto adjacente'))

hipotenusa = hypot(catetoOposto, catetoAdjacente)

print('Hipotenusa = {}'.format(hipotenusa))