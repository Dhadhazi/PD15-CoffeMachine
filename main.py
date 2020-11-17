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
    "money": 0
}


def drinkMaker(choice):
    global resources;
    for item in MENU[choice]["ingredients"]:
        resources[item] -= MENU[choice]["ingredients"][item]
    resources["money"] += MENU[choice]["cost"]
    print(f"Here is your {choice}. Enjoy!")


def coinProcessor(choice):
    total = int(input("how many quarters?") or "0")*0.25
    total += int(input("how many dimes?") or "0")*0.1
    total += int(input("how many nickles?") or "0")*0.05
    total += int(input("how many pennies?") or "0")*0.01
    change = total - MENU[choice]["cost"]
    if change < 0:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if change > 0:
            change = round(change, 2)
            print(f"Here is the ${change} back")
        return True



def resourceCheck(choice):
    for item in MENU[choice]["ingredients"]:
        if MENU[choice]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


choice = ""

while choice != "off":
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "report":
        print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: {money}")

    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if resourceCheck(choice):
            if coinProcessor(choice):
                drinkMaker(choice)

