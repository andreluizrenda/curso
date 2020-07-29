# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo. Calcule
# e mostre o comprimento da hipotenusa.
from math import hypot

oposto = float(input('Digite o valor do cateto oposto: '))
adjacennte = float(input('Digite o valor do cateto adjascente: '))

hipotenusa = hypot(oposto,adjacennte)

print("A hipotenusa vai medir {:.2f}".format(hipotenusa))