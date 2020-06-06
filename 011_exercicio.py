#aula 11 - exercicio
'''
Faça um programa que leia um numero inteiro menor que 1000
Imprima a quantidade de centenas, dezenas e unidades
Testar com 326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20
10, 21, 11, 1 , 7 e 16
Exemplos:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades
    
'''

numero = int(input("Digite um numero: "))

if numero > 1000:
    print("Numero invalido!")
    numero = int(input("Digite um numero: "))

centena = numero // 100
dezena = numero % 100 // 10
unidade = numero % 10 // 1

if centena > 1:
    centena_texto = "centenas"
else:
    centena_texto = "centena"

if dezena > 1:
    dezena_texto = "dezenas"
else:
    dezena_texto = "dezena"
    
if unidade > 1:
    unidade_texto = "unidades"
else:
    unidade_texto = "unidade"

print(centena,centena_texto,",",dezena,dezena_texto,"e",unidade,unidade_texto)

#print("{} Centena,{} Dezena e{} Unidade".format(centena,dezena,unidade))
#print(f"{centena} centena(s), {dezena} dezena(s) e {unidade} unidades(s)")
