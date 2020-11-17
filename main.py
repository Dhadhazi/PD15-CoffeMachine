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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resourceCheck(choice):
    if (MENU[choice]["ingredients"]["water"] > resources["water"]):
        return "Sorry there is not enough water."
    elif (MENU[choice]["ingredients"]["milk"] > resources["milk"]):
        return "Sorry there is not enough milk."
    elif (MENU[choice]["ingredients"]["coffee"] > resources["coffee"]):
        return "Sorry there is not enough coffee."
    else:
        return "all cool bro"

choice = ""

while choice != "off":
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = 0
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "report":
        print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: {money}")

    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        print(resourceCheck(choice))

