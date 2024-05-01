MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 500,
    "milk": 300,
    "coffee": 200,
}

total_collected = 0
# TODO: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”


def check_resources(ing):
    for ite in ing:
        if resources[ite] < ing[ite]:
            return False
    return True


def prepare_drink(choice):
    global resources
    print("Preparing your drink")
    for name in MENU[choice]["ingredients"]:
        resources[name] -= MENU[choice]["ingredients"][name]
    print("Enjoy your drink")


def get_cash(choice):
    global total_collected
    total_cash = 0
    total_cost = MENU[choice]["cost"]
    while total_cash < total_cost:
        remaining = total_cost - total_cash
        cash = int(input(f"Please insert cash, need ${remaining} : $ "))
        total_cash += cash
        if total_cost == total_cash:
            total_collected += total_cost
            prepare_drink(choice)
            print("Enjoy ur drink")
        elif total_cost < total_cash:
            print(f"Please take balance of {total_cash-total_cost}")
            total_collected += total_cost
            prepare_drink(choice)
        else:
            print("*******************")


machine_off = False


while not machine_off:
    users_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if users_choice == "off":
        machine_off = True
    elif users_choice == "report":
        print(resources, total_collected)
    else:
        for item in MENU:
            if item == users_choice:
                if check_resources(MENU[item]["ingredients"]):
                    get_cash(item)
                else:
                    print("Sorry not enough resources")



