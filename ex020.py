# Faça um programa que leia o nome de quatro alunos e realize sorteio da ordem de apresentação dos trabalhos.

import random
a1 = str(input('Digite o primeiro aluno: '))
a2 = str(input('Digite o segundo aluno: '))
a3 = str(input('Digite o terceiro aluno: '))
a4 = str(input('Digite o quarto aluno: '))

lista = [a1,a2,a3,a4]
random.shuffle(lista)

print('A ordem de apresentação será: ')
print(lista)