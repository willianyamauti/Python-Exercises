import math

def preencherVetor(valores, tipo):
    vetor = [ ]
    valores = valores.split(',')
    for i in range(len(valores)):
        if tipo == 'int':
            valor = int(valores[i].strip())
        elif tipo == 'float':
            valor = float(valores[i].strip())
        else:
            valor = valores[i].strip()
        vetor.append(valor)
    return vetor

def imprimeVetor(vetor):
    print('[', end='')
    if len(vetor) > 0:
        print(f' {vetor[0]}', end='')
        for i in range(1, len(vetor)):
            print(f', {vetor[i]}', end='')
    print(' ]', end='')


def criarVetor(qtdElementos, valorPadrao):
    vetor = [ ]
    for i in range(qtdElementos):
        vetor.append(valorPadrao)
    return vetor

def criarMatriz(qtdLinhas, qtdColunas, valorPadrao):
    matriz = [ ]
    for lin in range(qtdLinhas):
        linha = criarVetor(qtdColunas, valorPadrao)
        # for col in range(qtdColunas):
        #     linha.append(valorPadrao)
        matriz.append(linha)
    return matriz

def preencherMatriz(valores, tipo):
    matriz = []
    linhas = valores.split(';')
    for lin in range(len(linhas)):
        vetor = preencherVetor(linhas[lin], tipo)
        matriz.append(vetor)
    return matriz

def imprimeMatrizEmLinha(matriz):
    print('[', end='')
    if len(matriz) > 0:
        imprimeVetor(matriz[0])
        for lin in range(1, len(matriz)):
            print(', ', end='')
            imprimeVetor(matriz[lin])
        print(']', end='')

def imprimeMatriz(matriz):
    if len(matriz) > 0:
        imprimeVetor(matriz[0])
        print('')
        for lin in range(1, len(matriz)):
            imprimeVetor(matriz[lin])
            print('')

def converterVetorMatriz(vetor):
    indice_quadratico = int(math.sqrt(len(vetor)))
    matriz_qdt = []
    # divide o vetor de acordo com o indice quadratico e preenche a matriz
    for x in range(0, len(vetor), indice_quadratico):
        matriz_qdt.append(vetor[x:x + indice_quadratico])

    return matriz_qdt





numeros = input(f'Entrada do vetor: ')
print(f'Matriz correspondente:')
vet_numeros = preencherVetor(numeros, 'int')
matriz_quadratica = converterVetorMatriz(vet_numeros)
imprimeMatriz(matriz_quadratica)