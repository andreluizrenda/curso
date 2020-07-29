#Digite um ângulo e mostre o valor de seno, cosseno e tangente.
import math

angulo = float(input('Digite o valor do ângulo: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print("O valor do SENO do angulo {}° é {:.2f}".format(angulo, seno))
print("O valor do COSSENO do angulo {}° é {:.2f}".format(angulo, cosseno))
print("O valor do TANGENTE do angulo {}° é {:.2f}".format(angulo, tangente))