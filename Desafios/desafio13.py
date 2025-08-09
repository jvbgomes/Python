dias_alugados = int(input('Quantos dias foi alugado? '))
km = float(input('Quantos km foram rodados? '))
custo = (60 * dias_alugados) + (km * 0.15 )
print('O total a pagar será R${:.2f}. '.format(custo))