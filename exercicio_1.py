"""

Faça um programa que peça ao usuario um numero inteiro, e informe se ele é par ou ímpar.Caso o usuario nao digite
um numero inteiro, informe que nao é um numero inteiro

"""

num = input('Digite um número: ')

if num.isdecimal():

    num = int(num)
    par_impar = num % 2

    if par_impar == 0:
        print(f'O numero {num} é par')

    else:
        print(f'o numero {num} é impar')

else:
    print(f'Erro,{num} não é um numero valido,digite um numero inteiro!!!')