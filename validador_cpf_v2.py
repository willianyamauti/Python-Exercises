"""
CPF = 168.995.350-09
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""

while True:
    cpf = input('Digite o cpf: ')
    cpf = cpf.replace('.', '').replace('-', '')

    if not cpf.isnumeric() or len(cpf) != 11:
        print(f'CPF invalido digite novamente! '
              f'(o cpf deve não deve possuir letras e deve ter 11 numeros)')
        continue

    novo_cpf = cpf[:-2]
    fator = 11
    soma_digito_1 = 0
    soma_digito_2 = 0

    for index in range(0, 9, 1):
        soma_digito_1 += int(novo_cpf[index]) * (fator - 1)
        soma_digito_2 += int(novo_cpf[index]) * fator
        fator -= 1

    digito_ver_1 = 11 - (soma_digito_1 % 11)
    digito_ver_1 = 0 if digito_ver_1 > 9 else digito_ver_1  # se digito_ver > 9 -> 0
    digito_ver_2 = 11 - ((soma_digito_2 + (digito_ver_1 * 2)) % 11)
    digito_ver_2 = 0 if digito_ver_2 > 9 else digito_ver_2

    novo_cpf += str(digito_ver_1) + str(digito_ver_2)

    # retorna true para sequencias [ 11111111111,0000000000,...]
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    msg = 'Esse CPF é valido' if novo_cpf == cpf and not sequencia else 'Esse cpf é invalido'
    print(msg)
