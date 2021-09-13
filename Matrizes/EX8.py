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

def calcular_totalPontos(matriz_pontos):
    Pontos_porTime = criarVetor(len(matriz_pontos), 0)   # cria um vetor com a quantidade de produtos
    for linha in range(len(matriz_pontos)):
        for coluna in range(len(matriz_pontos[linha])):
           if matriz_pontos[linha][coluna] == 0 or matriz_pontos[linha][coluna] == 1:
               if matriz_pontos[linha][coluna] == 0:
                   Pontos_porTime[linha] += 1   #empate
               else:
                   Pontos_porTime[linha] += 3   #vitoria

    return Pontos_porTime

def escolher_timeVencedor(matriz_pontos):
    maior_pontuacao= 0
    indice_time = 0
    for time in range(len(matriz_pontos)):
        if matriz_pontos[time] > maior_pontuacao:
            maior_pontuacao = matriz_pontos[time]
            indice_time = time

    return indice_time

times = input('Nomes dos times: ')
resultados = input('Resultados dos jogos: ')
vet_times = preencherVetor(times, 'str')
mat_resultados = preencherMatriz(resultados, 'int')
resultados = calcular_totalPontos(mat_resultados)
time_vencedor = escolher_timeVencedor(resultados)
print(f'Time campeão: {vet_times[time_vencedor]}\n'
      f'Pontuação do campeão: {resultados[time_vencedor]}')
