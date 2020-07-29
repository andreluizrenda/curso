#Faça um programa que leia o nome de uma cidade e diga se ela começa com a palavra SANTO.

cidade = str(input('Qual a cidade que você nasceu? ')).strip()
print(cidade[:5].upper() == 'SANTO')
