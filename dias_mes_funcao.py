def e_bisexto (ano):
    """Retorna Falso para ano nao bisexto
       e Verdadeiro para ano bisexto """
    if ano % 4 != 0:
        return False

    else:
        if ano % 100 != 0:
            return True
        elif ano % 400 != 0:
            return False
        else:
            return True

#anos no formato 2XXX, e mes como respectivo numero
def dias_no_mes(ano,mes):
    """Retorna a quantidade de dias para o mes do ano escolhido """
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if e_bisexto(ano) and mes == 2:
        return 29
    else:
        return dias_mes[mes-1]

anos = int(input("Digite o ano: "))
mes = int(input("Digite o mês: "))
dias = dias_no_mes(anos, mes)
print(dias)