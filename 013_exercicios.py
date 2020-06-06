# aula 13 - Exercicios
'''
Dado um numero inteiro positivo n, calcular a soma dos n primeiros numeros
inteiros positivos
'''
#Código do exercicio
'''

n = int(input("Digite um numero: "))

cont = 0
prod = 0
while cont < n:
    prod = prod + cont
    cont = cont + 1
print("A soma dos numeros antecessores de",n,"eh:",prod)
'''

'''
Dado um numero, imprimir os n primeiros impares.
n = 4 --> 1 3 5 7
n = 3 --> 1 3 5
'''
# Código do exercicio
n = int(input("Digite um numero: "))

cont = 1

while cont < n:
    prod = cont
    print("Os numeros impares antecessores de",n,"eh:",prod)
    cont = cont + 2

