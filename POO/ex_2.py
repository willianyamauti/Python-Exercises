from prettytable import PrettyTable

tabela = PrettyTable()
tabela.field_names = ['Pokemon', 'Tipo']
tabela.add_rows(
    [
        ['Pikachu', 'Eletrico'],
        ['Squirtle', 'Agua'],
        ['Charmander', 'Fogo'],
    ]
)
tabela.align = "l"
print(tabela)
