#aula 13 - Ciclos de repetição - While
'''
Dada uma sequencia de numeros inteiro, seguida por 0, imprimir seus quadrados.

'''

print("Caso deseje encerrar digite 0 (zero)")

n = int(input("Digite o próximo numero: "))

while n != 0: 
    print(n,"ao quadrado =", n * n)
    n = int(input("Digite o próximo numero: "))
    

###################################################################
'''
Exercicio:
Dado um numero inteiro,, não negativo, determinar n! fatorial
5! = 5*4*3*2*1 = 120
3! = 3*2*1 = 6

n = int(input("Digite o numero: "))
'''
# Código do exercicio
'''
decrementando
prod = n
cont = n - 1

while cont > 1:
    prod = prod * cont
    cont = cont - 1

print(n,"! = ",prod)
'''

'''
#incrementando
prod = 1
cont = 2

while cont <= n:
    prod = prod * cont
    cont = cont + 1
print(n,"! = ",prod)
'''
###########################################
'''
Exercicio
Faça um programa que peça dois números, base e expoente.
Calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função potência da linguagem.
O número do expoente indica o número de vezes que a base é multiplicada
por ela mesma.
A potência é o número 1 * base * expoente N
2**3 = 1 * 2 * 2 * 2 = 8
2**0 = 1 * 2
'''
#Código do exercicio
'''
base = int(input("Digite o número da base: "))
expoente = int(input("Digite o número do expoente: "))

cont = 0
produto = 1

while cont < expoente:
    produto = produto * base
    cont = cont + 1

print(base, "elevado a",expoente, "=", produto)
'''