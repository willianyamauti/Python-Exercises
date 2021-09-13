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

def menor_nota(matriz,tipo):
    nota = matriz[0][0]
    if tipo != 'str':
        for linha in range(len(matriz)):
            for coluna in range(len(matriz[linha])):
                if matriz[linha][coluna] < nota:
                    nota = matriz[linha][coluna]


    else:
        """ 
            ord() retorna o valor inteiro do unicode da letra, no caso alfabetico, 'a' teria um valor menor que 'b',
            assim sucessivamente

        """
        for linha in range(len(matriz)):
            for coluna in range(len(matriz[linha])):
                if ord(matriz[linha][coluna]) > ord(nota):
                    nota = matriz[linha][coluna]

    return nota

notas = input('Notas dos alunos: ')
tipo = input('Tipo de nota: ')
if tipo != 'int':
    if tipo == 'real':
        tipo = 'float'
    else:
        tipo = 'str'
matriz_notas = preencherMatriz(notas, tipo)
pior_nota = menor_nota(matriz_notas, tipo)
print(f'Pior nota: {pior_nota}')
