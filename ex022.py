#Leia o nome comploet e coloque todas as letras em maiusculas, minusculas, quantas letras sem espaço, primeiro nome
#e a quantidade de letras no primeiro nome.

nome = str(input('Digite o seu nome completo: ')).strip()

print('..:Analisando seu nome..:')
print('O seu nome em maiuscula, ficou {}'.format(nome.upper()))
print('O seu nome em minuscula, ficou {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('O seu primeiro é {} e ele tem {} letras'.format(separa[0], len(separa[0])))