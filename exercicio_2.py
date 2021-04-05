"""

Faça um programa que pergunte a hora ao usuario e, baseando-se no horario desrito exiba uma saudação apropriada.
Ex: 0 - 11 bom dia, boa tarde 12 - 17, boa noite 18 - 23

"""

horario = input('Qual o horario?')

if horario.isdigit():

    horario = int(horario)

    if horario < 0 or horario > 23:
        print(f'o horario {horario} é ivalido escolha um numero inteiro entre 0 e 23')

    else:

        if horario <= 11:
            print(f'BOM DIA!')

        # como o algoritmo ja passou pelo primeiro if nao tem necessidade de (horario > 11 e <= 17)
        elif horario <= 17:
            print(f'BOA TARDE!')

        else:
            print(f'BOA NOITE!')

else:
    print(f'Erro,{horario} não é um numero valido,digite um numero inteiro!!!')