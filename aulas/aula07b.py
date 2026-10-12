#nome=input('Qual o seu nome? ')
#print("E um prozer te conhecer {}!".format(nome))
#print("E um prozer te conhecer {:-^20}!".format(nome))

n1=int(input('Digite um valor'))
n2=int(input('Digite outro numero!'))
s=n1+n2
sub=n1-n2
m=n1*n2
d=n1/n2
p=n1**n2
di=n1//n2
rd=n1%n2
print('A soma é: {}, o produto è: {},e a subtração e: {}, concluindo com resultado da divisão que é: {:.3}'.format(s,m,sub,d), end=' ')
print('E a potencia e: {}, a divisão inteira é: {}, o resto da didisão è: {}'.format(p,di,rd))
