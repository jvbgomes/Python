import math
angulo = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O seno de 30 é {:.2f}, \no cosseno é {:.2f} e \na tangente é {:.2f} '.format(seno, cos, tan))