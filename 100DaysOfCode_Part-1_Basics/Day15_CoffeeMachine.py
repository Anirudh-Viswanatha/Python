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

# TODO : 1: input what would you like? (espresso/latte/cappuccino):
# TODO : 2: insert coins, SUM THE COINS, calculate balance and return balance
# TODO : 3: validate enough resources are there
# TODO : 4: Either give coffee or not give coffee and print message
# TODO : 5: repeat

remaining_water = (resources["water"])
remaining_coffee = (resources["coffee"])
remaining_milk = (resources["milk"])
profit = 0

def coffee_inputs():
  print("Please insert coins.")
  quarters = int(input("how many quarters?: "))
  dimes = int(input("how many dimes?: "))
  nickles = int(input("how many nickles?: "))
  cents = int(input("how many cents?: "))
  global totalmoney
  totalmoney = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (cents * 0.01)


def pour_coffee():
    global remaining_water
    global remaining_milk
    global remaining_coffee

    # print(f"water remaining: {remaining_water}")
    # print(f"water required for {coffee}: {(MENU[coffee]["ingredients"]["water"])}")
    # print(f"milk remaining: {remaining_milk}")
    # # print(f"milk required for {coffee}: {(MENU[coffee]["ingredients"]["milk"])}")
    # print(f"coffee remaining: {remaining_coffee}")
    # print(f"coffee required for {coffee}: {(MENU[coffee]["ingredients"]["coffee"])}")

    if coffee == "latte" or coffee == "cappuccino":
        global profit
        if remaining_water >= (MENU[coffee]["ingredients"]["water"]) and remaining_coffee >= (MENU[coffee]["ingredients"]["coffee"]) and remaining_milk >= (MENU[coffee]["ingredients"]["milk"]):
            print(coffee_inputs())
            if (totalmoney > MENU[coffee]["cost"]):
                balancemoney = round(totalmoney - MENU[coffee]["cost"], 2)
                print(f"Here is the balance amount: {balancemoney}")
                print(f"Here is your {coffee} ☕️. Enjoy!")
                remaining_water = remaining_water - (MENU[coffee]["ingredients"]["water"])
                remaining_coffee = remaining_coffee - (MENU[coffee]["ingredients"]["coffee"])
                remaining_milk = remaining_milk - (MENU[coffee]["ingredients"]["milk"])
                profit += MENU[coffee]["cost"]
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough resources.")
    elif coffee == "espresso":
        if remaining_water >= (MENU[coffee]["ingredients"]["water"]) and remaining_coffee >= (MENU[coffee]["ingredients"]["coffee"]):
            print(coffee_inputs())
            if (totalmoney > MENU[coffee]["cost"]):
                balancemoney = round(totalmoney - MENU[coffee]["cost"], 2)
                print(f"Here is the balance amount: {balancemoney}")
                print(f"Here is your {coffee} ☕️. Enjoy!")
                remaining_water = remaining_water - (MENU[coffee]["ingredients"]["water"])
                remaining_coffee = remaining_coffee - (MENU[coffee]["ingredients"]["coffee"])
                profit += MENU[coffee]["cost"]
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough resources.")
    elif coffee == "report":
        print(f"water remaining: {remaining_water}ml")
        print(f"milk remaining: {remaining_milk}ml")
        print(f"coffee remaining: {remaining_coffee}g")
        print(f"profit: ${profit}")


should_continue = True

while should_continue:
    coffee = input("what would you like? (espresso/latte/cappuccino): ")
    if coffee == "off":
        should_continue = False
    else:
        pour_coffee()
else:
    should_continue = False


#-----------------------------------------------------------------------------------

# OPTIMIZED - OPTION 2


# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# profit = 0
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }


# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"​Sorry there is not enough {item}.")
#             return False
#     return True


# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total


# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False


# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️. Enjoy!")


# is_on = True

# while is_on:
#     choice = input("​What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])








