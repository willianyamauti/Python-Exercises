def imprimir_dicionario(dicionario):
    for chave in dicionario:
        print(chave)
        print(dicionario[chave])


def atribuir_resultados(nota_estudantes, resultado_estudantes):
    for chave in nota_estudantes:
        resultado = nota_estudantes[chave]
        if resultado <= 70:
            resultado_estudantes[chave] = "Reprovado"
        elif 70 < resultado <= 80:
            resultado_estudantes[chave] = "Aceitavel"
        elif 80 < resultado <= 90:
            resultado_estudantes[chave] = "Ultrapassou expectativas"
        else:
            resultado_estudantes[chave] = "Expetacular"


notas_estudantes = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
resultados_estudantes = {}


atribuir_resultados(notas_estudantes, resultados_estudantes)
imprimir_dicionario(resultados_estudantes)
