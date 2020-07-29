#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere o dólar em R$ 5.27

real = float(input('Quando dinheiro você tem na carteira? R$ '))
valor_dolar = 5.27
dolar = real / valor_dolar

print('\nCom R$ {:.2f} você pode comprar US$ {:.2f}'.format(real,dolar))
print('\nValor do dolar atualmente R$ {:.2f}'.format(valor_dolar))



