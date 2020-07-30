#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
#ou não formar um triângulo.

print('.::. '*15)
print('\t\t...Análise se é possível formar um triângulo...')
print('.::. '*15)
a = int(input('Digite o primeiro seguimento: '))
b = int(input('Digite o segundo seguimento: '))
c = int(input('Digite o terceiro seguimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos de reta acima PODEM formar um TRIÂNGULO!')
else:
    print('Os seguimentos de reta acima NÃO PODEM formar um TRIÂNGULO!')
