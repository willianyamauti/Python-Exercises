diario_viagem = [
    {
        "país": "França",
        "visitas": 12,
        "cidades": ["Paris", "Lille", "Dijon"]
    },
    {
        "país": "Germany",
        "visitas": 5,
        "cidades": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def adicionar_novo_pais(pais, visitas, cidades):
    novo_pais = {
        "país": pais,
        "visitas": visitas,
        "cidades": cidades
    }
    diario_viagem.append(novo_pais)


adicionar_novo_pais("Russia", 2, ["Moscou", "Sao Petersburgo"])
print(diario_viagem)
