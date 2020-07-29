#Crie um programa que leia um numero qualquer pelo teclado e mostre na tela a sua porção inteira.
#Exemplo: 6.127 deve mostrar 6

import math

numero = float(input('Digite um numero qualquer: '))

print('O numero é {} e a parte real dele é {}'.format(numero,math.floor(numero)))