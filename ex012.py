#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Qual o preço do produto? R$ '))
desconto = float(input('Qual o valor do desconto? '))

valor_final = preço - (preço*desconto/100)

print("O preço era R$ {:.2f} você deu {}% de desconto e o preço final é R$ {:.2f}".format(preço, desconto, valor_final))