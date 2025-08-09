medida = float(input('Digite um valor em metros: '))
cm = 100 * medida
dm = 10 * medida
mm = 1000 * medida
dam = float(0.1 * medida)
hm = float(0.01 * medida)
km = float(0.001 * medida)
print('O valor em metros é {}m. \nJá em centímetros é {:.0f}cm e em milímetros é {:.0f}mm. '.format(medida, cm, mm))
print('Os {}m são equivalentes a {}dam. \nJá {}m em hectômetro é {}hm e em kilômetro é {}km. '.format(medida, dam, medida, hm, km))