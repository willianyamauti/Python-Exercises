def simular_retorno(investimento, tempo):
    #formula utilizada capital*taxa*tempo
    if investimento <= 100000:
        return investimento * 0.06 * tempo
    else:
        return investimento * 0.0675 * tempo

print(f'Simulador de retorno de investimento inicial')
capital = float(input('Digite o capital a ser investido: '))
tempo = int(input('Digite a quantodade de meses: '))
montante = simular_retorno(capital, tempo)
print(montante)
print(f'Ao investir R${capital:.2f}, após {tempo} meses você tera um lucro de R${(montante):.2f},'
      f' totalizando o valor de R${capital + montante:.2f}.')