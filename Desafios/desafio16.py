#from math import sqrt
#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto adjacente: '))
#h = (co**2 + ca**2) ** (1/2)
#print('O cateto oposto é {} e p cateto adjacente é {}, então a hipotenusa é {:.2f}.'.format(co, ca, h))

import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = math.hypot(co, ca)
print('A hipotenusa é {:.2f}. '.format(h))