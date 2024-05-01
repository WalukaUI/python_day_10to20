from menu import MenuItem, Menu
from coffie_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine = MoneyMachine()
my_coffie_maker = CoffeeMaker()
my_menu = Menu()

redo = True
while redo:
    options = my_menu.get_items()
    print(options)
    names = input("please select the drink?")
    if names == "end":
        redo = False
    elif names == "report":
        my_coffie_maker.report()
        my_money_machine.report()
    elif names == "off":
        redo = False
    else:
        drink = my_menu.find_drink(names)
        if drink:
            resources = my_coffie_maker.is_resource_sufficient(drink)
            if resources:
                money = my_money_machine.make_payment(drink.cost)
                if money:
                    my_coffie_maker.make_coffee(drink)
