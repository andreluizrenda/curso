#Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar.

numero = int(input('Digite um numero: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é par!'.format(numero))
else:
    print('O número {} é ímpar!'.format(numero))