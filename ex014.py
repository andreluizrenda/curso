# Faça um programa que converta uma temperatura digitada em graus celsius para fahrenheit.
temperatura = float(input('Qual a temperatura em graus Celsius? '))

calculo = 32 + 9 * temperatura / 5

print('A temperatura {}°C é igual a {}°F'.format(temperatura, calculo))