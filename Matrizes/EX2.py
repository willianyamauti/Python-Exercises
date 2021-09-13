# import biblioteca_matriz as mtz_bib

# confere se todas a matriz tem o mesmo numero de questoes do gabarito
# retorna False caso o numero de questoes for imcompativel e True caso for

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
            return True
    return False

def notasAlunos(gabarito, matriz_alunos):
    vet_notasAlunos = []
    for aluno in range(len(matriz_alunos)):
        acertos = 0
        for questao in range(len(matriz_alunos[aluno])):
            if matriz_alunos[aluno][questao] == gabarito[questao]:
                acertos +=1
        vet_notasAlunos.append((acertos*10)/len(gabarito))
    return vet_notasAlunos


print(f'Notas de BCC701')
gabarito = input('Digite o gabarito:\n')
# gabarito ='D, A, C, E, E'
vet_gabarito = preencherVetor(gabarito, 'str')
notas_alunos = input('Digite as respostas dos alunos:\n')
#respostas_alunos = 'D, A, C, C, E; D, A, C, E, A; D, A, C, E, E; E, A, C, E, E; E, E, E,A, A; A, B, B, E, C; D, D, C, C, E'
matriz_notas_alunos = preencherMatriz(notas_alunos, 'str')

if notas_alunos == '':
    print('\nNenhum aluno para avaliar')

elif compatibilidade_inputs(vet_gabarito, matriz_notas_alunos):
    print('\nQuantidade de questões incompatível')

else:
    print('Notas dos alunos:\n')
    notas_alunos = notasAlunos(vet_gabarito, matriz_notas_alunos)
    imprimeVetor(notas_alunos)


# if matriz_notas_alunos == '':
#     print('Nenhum aluno para avaliar')
#     quit()
#
# matriz_notas_alunos = preencherMatriz(matriz_notas_alunos, 'str')
# chama a função para conferir o num de questoes, entra no if se o retorno for false
# if not compatibilidade_inputs(vet_gabarito, matriz_notas_alunos):
#     print('Quantidade de questões incompatível')
#     quit()
#
# notas_alunos = notasAlunos(vet_gabarito, matriz_notas_alunos)
# imprimeVetor(notas_alunos)


