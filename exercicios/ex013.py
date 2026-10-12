print('Calculador de reajuste salarial ')
s=float(input("Qual o seu salario atual? ").replace(',','.'))
d=int(input('qual foi a porcentagem do reajuste? '))
print(f'o valor do seu salario coom o reajuste e: {s + (s * d/100):.2f}')