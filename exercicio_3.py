"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

primeiro_nome = input('Digite seu primeiro nome: ')
qtd_letras = len(primeiro_nome)

if qtd_letras <= 4:
    print(f'Seu nome é curto.')

elif qtd_letras <=6:
    print(f'Seu nome é normal.')

else:
    print(f'Seu nome é muito grande.')
