# import biblioteca_matriz as mtz_bib
# importando as funções da biblioteca de matriz,para usar basta digitar "matr." e depois o nome da função

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
        print(f' {vetor[0]:.2f}', end='')
        for i in range(1, len(vetor)):
            print(f', {vetor[i]:.2f}', end='')
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

# busca em toda matrix o menor valor numerico e retorna seu indice
def linhaMenorValor(matriz):
    menor_valor = matriz[0][0]
    indice_min = 0
    for lin in range(len(matriz)):
        for col in range(len(matriz[lin])):
            if matriz[lin][col] < menor_valor:
                menor_valor = matriz[lin][col]
                indice_min = lin
    return indice_min


# busca na linha que possui o menor valor, pelo maior valor numerico
def colunaMaiorValor(matriz, index_min):
    maior_valor = 0
    indice_max = 0
    for elemento in range(len(matriz[index_min])):
        if matriz[index_min][elemento] > maior_valor:
            maior_valor = matriz[index_min][elemento]
            indice_max = elemento
    return indice_max

# main

print(f'MixMax em uma Matriz')
#criandoa a matriz com o input desejado
matriz_MinMax = preencherMatriz(input('valores da matriz:\n'), 'int')
linha_min = linhaMenorValor(matriz_MinMax)
coluna_max = colunaMaiorValor(matriz_MinMax, linha_min)
print(f'MinMax: [{linha_min}, {coluna_max}] = {matriz_MinMax[linha_min][coluna_max]}')

40, 85, 74, 60, 36, 55; 8, 31, 37,82, 47, 88; 30, 48, 52, 90, 26, 2; 57, 73,10, 41, 61, 81; 87, 1, 14, 68, 64, 7; 56,28, 21, 86, 6, 93; 43, 18, 42, 62, 5, 99;92, 54, 69, 50, 67, 70; 97, 32, 46, 77,58, 94