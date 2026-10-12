n = int(input("Qual numero você desejá?"))
print(f'você escolheu o numero: {n}, então o dobro e {n * 2}.')
print(f'O triplo e {n * 3}, e a raiz quadrada e {n ** (1/2):.2f}.')

#OU USANDO O INPORT MATH
#EX:
import math

n2 = int(input("Qual numero você desejá?"))
print(f'você escolheu o numero: {n2}, então o dobro e {n2 * 2}.')
print(f'O triplo e {n2 * 3}, e a raiz quadrada e {math.sqrt(n2):.2f}.')