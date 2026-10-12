print('Bem vinda ao seu calculador de preço com 5% de descondo')
p= int (input("Insira o preço anterior ao desconto: "))
d=5
print(f'O preço final e: {p - (p * d / 100):.2f}')