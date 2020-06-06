# Aula 07 - Inputs
'''
numero_1 = int(input("Digite o primeiro numero: "))
numero_2 = int(input("Digite o segundo numero: "))

print(numero_1,"+",numero_2,"=",numero_1+numero_2)
print(numero_1,"-",numero_2,"=",numero_1-numero_2)
print(numero_1,"*",numero_2,"=",numero_1*numero_2)
print(numero_1,"/",numero_2,"=",numero_1/numero_2)
print(numero_1,"//",numero_2,"=",numero_1//numero_2)
'''

nota1 = int(input("Digite a nota do primeiro bimestre: "))
nota2 = int(input("Digite a nota do segundo bimestre: "))
nota3 = int(input("Digite a nota do terceiro bimestre: "))
nota4 = int(input("Digite a nota do quarto bimestre: "))

print("A media do aluno foi: ",(nota1+nota2+nota3+nota4)/4)

print("\n\n")

valor_hora = int(input("Digite o valor que voce ganha por hora: "))
quantidade_horas = int(input("Digite a quantidade de horas trabalhadas no mes: "))

print("O seu salario total eh: ",valor_hora*quantidade_horas)