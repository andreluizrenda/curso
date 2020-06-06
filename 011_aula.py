# aula 11 - estruturas de decisão
# if, elif e else

'''
Faça um programa que peça 3 numeros e mostre em ordem decrescente.
'''

a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))

if a >= b >= c:
    print(a, b, c)
elif a >= c >= b:
    print(a, c, b)
elif b >= a >= c:
    print(b, a, c)
elif b >= c >= a:
    print(b, c, a)
elif c >= a >= b:
    print(c, a, b)
else:
    print(c, b, a)



'''
Maneira menos prática
if a < b:
    if a < c:
        if b < c:
            print(c , b, a)
        else:
            print(b, c, a)
    else:
        print(b, a, c)
'''
#################################################################
'''
Maneira mais limpa

dia = int(input("Digite o dia da semana: "))

if dia  == 1:
    print("Domingo")
elif dia  == 2:
    print("Segunda")
elif dia  == 3:
    print("Terça")
elif dia  == 4:
    print("Quarta")
elif dia  == 5:
    print("Quintauinta")
elif dia  == 6:
    print("Sexta")
elif dia  == 7:
    print("Sábado")
else:   
    print("Entrada inválida!")
'''
###########################################################
'''
Maneira suja de se fazer....

verifica = False

if dia  == 1:
    print("Domingo")
    verifica = True
if dia  == 2:
    print("Segunda")
    verifica = True
if dia  == 3:
    print("Terça")
    verifica = True
if dia  == 4:
    print("Quarta")
    verifica = True
if dia  == 5:
    print("Quintauinta")
    verifica = True
if dia  == 6:
    print("Sexta")
    verifica = True
if dia  == 7:
    print("Sábado")
    verifica = True

if verifica != True:    
    print("Entrada inválida!")
'''