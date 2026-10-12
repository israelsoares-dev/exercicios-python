m = float(input('Insira a sua medida em metros: '))
print('A medida selecionada foi {} metros! '.format(m))
print(f'Tem exatos {m * 100} centimetros e {m * 1000} milimetros! ')

#OU

m = float(input('Insira a sua medida em metros: ').replace(',', '.'))
cm = m*100
ml = m*1000
print(f'Tem exatos {cm:.0f} centímetros e {ml:.0f} milímetros! ')
