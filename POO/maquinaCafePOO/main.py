from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

desligar = False
menu = Menu()
maquina_moedas = MoneyMachine()
maquina_cafe = CoffeeMaker()

while not desligar:
    opcao = input(f"Digite sua escolha: {menu.get_items()}")
    pedido = menu.find_drink(opcao)
    if pedido is None:
        try:
            if opcao == 'report':
                maquina_cafe.report()
                maquina_moedas.report()
            elif opcao == 'off':
                desligar = True
            else:
                print("Opção inválida! Tente novamente...")
        except Exception as error:
            print(error)
    else:
        if maquina_cafe.is_resource_sufficient(pedido):
            if maquina_moedas.make_payment(pedido.cost):
                maquina_cafe.make_coffee(pedido)

