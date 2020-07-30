#Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço de passagem, cobrando
#R$ 0,50 km para viagem de até 200km e R$ 0,45 para viagens mais longas

distancia = float(input('Digite a distância da viagem em km: '))

'''
if distancia <= 200:
    calculo = distancia * 0.50
    
else:
    calculo = distancia * 0.45
'''

calculo = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print("Para a distância de {:.0f}km, o valor da passagem é R$ {:.2f}".format(distancia, calculo))