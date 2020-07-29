#Faça um programa que sorteie quatro alunos, escrevendo o nome dos alunos e na tela mostre o escolhido.
import random

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

lista = [aluno1,aluno2,aluno3,aluno4]
escolhido = random.choice(lista)

print('O aluno escolhido foi {}'.format(escolhido))