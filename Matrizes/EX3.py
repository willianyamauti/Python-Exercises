# import biblioteca_matriz as mtz_bib

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


def compatibilidade_inputs(vetor, matriz):
    for elementos in range(len(matriz)):
        if not len(matriz[elementos]) == len(vetor):
            return False
    return True

def calculaConsumos(vet_capcaidadeCarros, matriz_motoristas):
    matriz_consumo = []
    for motorista in range(len(matriz_motoristas)):
        vet_consumo = []
        for carro in range(len(matriz_motoristas[motorista])):
            vet_consumo.append(matriz_motoristas[motorista][carro] / vet_capcaidadeCarros[carro])
        matriz_consumo.append(vet_consumo)
    return matriz_consumo




print(f'Teste de consumo')
capacidadeTanques = input('Capacidade dos tanques:\n')
if not capacidadeTanques == '':
    vet_capacidadeTanques = preencherVetor(capacidadeTanques, 'int')
    kmPorCondutores = input('Quilometragens dos condutores:\n')
    if kmPorCondutores == '':
        print('\nDeve haver pelo menos um condutor')
    else:
        matriz_kmPorCondutores = preencherMatriz(kmPorCondutores, 'int')
        if not compatibilidade_inputs(vet_capacidadeTanques, matriz_kmPorCondutores):
            print('\nQuantidade de automóveis incompatível')
        else:
            matriz_condutores = calculaConsumos(vet_capacidadeTanques, matriz_kmPorCondutores)
            print('Consumos km/l:\n')
            imprimeMatriz(matriz_condutores)
else:
    print('\nE necessário pelo menos um automóvel')
