# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 m².

largura = float(input('Digite a largura da parede: ')) 
altura = float(input('Digite a altura da parede: '))
tintura = float(input('Digite a quantidade de litro que a lata de tinta consegue pintar: '))

area = largura * altura

tinta = area / tintura
print('\nSua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(largura, altura, area))
print('\nVocê precisará de {}l de tinta'.format(tinta))