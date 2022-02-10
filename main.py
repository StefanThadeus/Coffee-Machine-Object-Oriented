from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_work = True

while machine_work:
    beverage_input = input(f"What would you like? ({menu.get_items()}): ").lower()

    if beverage_input == "off":
        machine_work = False

    elif beverage_input == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        beverage = menu.find_drink(beverage_input)

        if beverage is not None:
            if coffee_maker.is_resource_sufficient(beverage) and money_machine.make_payment(beverage.cost):
                coffee_maker.make_coffee(beverage)
