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

def calcular_totalVendas(matriz_vendas):
    vendas_totais = criarVetor(len(matriz_vendas), 0)   # cria um vetor com a quantidade de produtos
    for linha in range(len(matriz_vendas)):
        for coluna in range(len(matriz_vendas[linha])):
            vendas_totais[linha] += matriz_vendas[linha][coluna] # soma todas as vendas do produto

    return vendas_totais

def escolher_produtoPromocional(matriz_totalVendas):
    maior_venda = 0
    indice_produto = 0
    for produto in range(len(matriz_totalVendas)):
        if matriz_totalVendas[produto] > maior_venda:
            maior_venda = matriz_totalVendas[produto]
            indice_produto = produto

    return indice_produto

produtos = input('Nomes dos produtos: ')
qtd_vendas = input('Quantidades de vendas: ')
vet_produtos = preencherVetor(produtos, 'str')
matriz_vendas = preencherMatriz(qtd_vendas, 'int')
total_vendaPorProduto = calcular_totalVendas(matriz_vendas)
produto = escolher_produtoPromocional(total_vendaPorProduto)
print(f'Produto selecionado: {vet_produtos[produto]}\n'
      f'Total de vendas do produto: {total_vendaPorProduto[produto]}')

