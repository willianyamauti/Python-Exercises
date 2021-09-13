import random
import string   #usar as funcoes string.ascii_letters, string.digits, strings.ponctuation

while True:
    configuracao_qtd_letras = input('Digite a quabtidade de letras desejadas: ')
    configuracao_qtd_simbolos = input('Digite a quantidade de simbolos desejada: ')
    configuracao_qtd_numeros = input('Digite a quantidade de numeros desejados: ')

    if not configuracao_qtd_simbolos.isnumeric() and configuracao_qtd_numeros.isnumeric() and configuracao_qtd_letras.isnumeric():
        print('Inavalido! Digite um numero inteiro maior que 1')
        continue
    if not (int(configuracao_qtd_simbolos) + int(configuracao_qtd_letras) + int(configuracao_qtd_numeros)) >= 3:
        print('Inavalido! Digite um numero inteiro maior que 1')
        continue

    configuracao_qtd_numeros = int(configuracao_qtd_numeros)
    configuracao_qtd_letras = int(configuracao_qtd_letras)
    configuracao_qtd_simbolos = int(configuracao_qtd_simbolos)
    senha = []

    for n in range(configuracao_qtd_simbolos):
        senha += random.choice(string.punctuation)
    for n in range(configuracao_qtd_numeros):
        senha += random.choice(string.digits)
    for n in range(configuracao_qtd_letras):
        senha += random.choice(string.ascii_letters)

    print(senha)
    random.shuffle(senha)
    senha = ''.join(senha)
    print(senha)
