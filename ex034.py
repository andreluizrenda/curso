#Escreva um programa que pergunte o salário de funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$ 1250, aumenta 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o salário do funcionário: R$ '))

if salario <= 1250:
    aumento = 15
    novo = salario + salario * aumento / 100
else:
    aumento = 10
    novo = salario + salario * aumento / 100 

print('Para o salário R$ {:.2f}, terá um aumento de {}% e o novo salário será de R$ {:.2f}'.format(salario, aumento, novo))

