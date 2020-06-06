#aula 10 - exercicio

'''
Faça um programa para um caixa eletronico, onde deverá informar o valor
do saque e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
Mínimo para saque: 10 reais || Máximo para saque: 600 reais

Exemplo 1: para sacar a quantia de 256 reais, deve fornecer
    2 x 100, 1 x 50, 1 x 5, 1 x 1
Exemplo 2: para sacar a quantia de 399 reais, deve fornecer
    3 x 100, 3 x 10, 1 x 5, 4 x 1
'''

print("Notas disponíveis para saque: 1, 5, 10, 50, 100")
print("Valor mínimo para saque: R$ 10,00")
print("Valor máximo para saque: R$ 600,00")
print("\n")

valor = int(input("Digite o valor para saque: "))

cem = valor // 100
cinquenta = valor % 100 // 50
dez = valor % 50 // 10
cinco = valor % 10 // 5
um = valor % 5 // 1

if 9 < valor < 601:

    print("Você recebeu",cem,"nota(s) de R$ 100")
    if valor % 100 >0:
        print("Você recebeu",cinquenta,"nota(s) de R$ 50")
        if valor % 50 > 0:
            print("Você recebeu",dez,"nota(s) de R$ 10")
            if valor % 10 >0:
                print("Você recebeu",cinco,"nota(s) de R$ 5")
                if valor % 5 >0:
                    print("Você recebeu",um,"nota(s) de R$ 1")

    
else:
    print("Valor fora do range disponível. Digite outro valor!")
