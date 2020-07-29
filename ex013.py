#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

salario = float(input('Qual o salário do funcionário? R$ '))
aumento = float(input('Qual o percentual de aumento para o funcionário? '))

novo_salario = salario + (salario * aumento / 100)

print("O salário antigo era R$ {:.2f}, o percentual de aumento foi de {}% e o novo salário é R$ {:.2f}".format(salario, aumento, novo_salario))