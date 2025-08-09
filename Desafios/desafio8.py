valor = float(input('Quanto de dinheiro você tem na carteira? R$'))
print('Com R${} você pode comprar US${:.2f} e €{:.2f}'.format(valor, valor/5.58, valor/6.37))