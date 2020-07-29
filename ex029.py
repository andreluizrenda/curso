#Faça um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem que ele foi multado.
#A multa vai custar R$ 7,00 por cada km acima do limite.

velocidade = float(input('Digite a velocidade do carro: '))

if velocidade > 80:
    multa = (velocidade-80) * 7
    print('Sua velocidade {:.0f}km/h está acima do permitido {}km/h.'.format(velocidade, 80))
    print('Você foi multado no valor de R$ {:.2f}.'.format(multa))
else:
    print('Sua velocidade {:.0f}km/h está dentro do limite estabelecido {}km/h. Tenha um bom dia!'.format(velocidade,80))