largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura * altura
tinta = 2 / area
print('A área da parede é {:.0f}m² e a quantidade de tinta necessária será {:.0f}l.'.format(area, tinta))