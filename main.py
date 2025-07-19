# Coffee Project

import math
from coffee_data import commands
from coffee_data import machine
from coffee_data import menu


# vars


coins = {
    "quarters": 0,
    "dimes": 0,
    "nickles": 0,
    "pennies": 0,
}


# functions


def clr():
    print('\n' * 20)


def reset_coins():
    global coins
    coins = {
        "quarters": 0,
        "dimes": 0,
        "nickles": 0,
        "pennies": 0,
    }


def ask_for_order():
    options = " | ".join([f"{n} (${menu[n]["price"]:.2f})" for n in menu.keys()])
    order = input(f"The machine offers: \n\n{options}\n\nWhat would you like to have? : ")

    allowed = []
    for n in commands:
        allowed.append(commands[n]["command"])

    while order not in menu.keys() and order not in allowed:
        print("Invalid option. Try again:")
        order = input(f"What would you like? ({options}): ")
    return order


def show_report():
    print("Current machine's resources:\n")
    for item in machine:
        value = machine[item]
        if item == "money":
            print(f"{item.capitalize()}: ${value:.2f}")
        else:
            print(f"{item.capitalize()}: {value}")

    print("\n")


def check_for_resources(order):
    """Kontroluje, jestli je v přístroji dostatek zdrojů a vrací na základě objednávky
    True nebo False, jestli je s momentálním stavem zdrojů možné objednávku provést či nikoliv."""
    clr()
    print(f"So you wanted {order}?")
    print("You will need:\n")

    is_order_possible = True
    ingredients = menu[order]["ingredients"]

    for item in ingredients:
        str = f"{item.capitalize()}: {ingredients[item]}"
        if ingredients[item] > machine[item]:
            is_order_possible = False
            str += f" (not enough {item}.)"
        print(str)

    print('\n')
    return is_order_possible


def get_input_number(s):
    """Vylepšený input, neustále nabízí input, dokut není zadána číselná hodnota int."""
    while True:
        n = input(s)
        try:
            n = int(n)
            break
        except ValueError:
            print("Not a number, try again.")
    return n


def get_coins_number(coins):

    """Vrací číselnou hodnotu na základě počtu jednotlivých mincí, které jsou uloženy
    v globální proměnné coins"""
    return coins["quarters"] * 0.25 + coins["dimes"] * 0.10 + coins["nickles"] * 0.05 + coins["pennies"] * 0.01


def show_current_coins(coins):

    """jednoduchá funkce, která vypíše číselnou hodnotu v $ dle dictionary coins, 
    ve kterém jsou uloženy jednotlivé mince"""
    print(f"Inserted: ${get_coins_number(coins):.2f}")


def get_remain_coins(coins, p_price):

    """vrací počet jednotlivých mincí ve formě dictionary coins, které zbyly po platbě"""
    sum = get_coins_number(coins)
    remain = (sum - p_price) * 100

    q = math.floor(remain / 25)
    remain -= q * 25
    d = math.floor(remain / 10)
    remain -= d * 10
    n = math.floor(remain / 5)
    remain -= n * 5
    p = math.floor(remain)

    return {
        "quarters": q,
        "dimes": d,
        "nickles": n,
        "pennies": p,
    }


def show_remain_coins(remain_coins):
    s = ", ".join([f"{remain_coins[n]} {n}" for n in remain_coins])
    print(f"Here are your coins back: ( {s} )")


def pay_for_order(coins, p_order):
    price = menu[p_order]["price"]
    print(f"Your order is: {p_order.capitalize()} (cost ${price:.2f})")
    print("Please, insert coins:\n")

    for item in coins:
        coins[item] = get_input_number(f"Insert {item}: ")
        show_current_coins(coins)

        if get_coins_number(coins) == price:
            print(f"\nThank you, you paid ${price:.2f}")
            return True

        elif get_coins_number(coins) > price:
            print(f"\nThank you, you paid ${get_coins_number(coins):.2f}. "
                  f"\nPlease wait, we will return your change (${(get_coins_number(coins) - price):.2f}).")
            remain_coins = get_remain_coins(coins, price)
            show_remain_coins(remain_coins)
            return True

    print(f"\nWe are sorry, but you inserted an insufficient amount in coins (${get_coins_number(coins):.2f}), "
          f"your money will be returned:")
    show_remain_coins(coins)


def consume_resources(order):
    machine['water'] -= menu[order]["ingredients"]["water"]
    machine['milk'] -= menu[order]["ingredients"]["milk"]
    machine['coffee'] -= menu[order]["ingredients"]["coffee"]
    machine['money'] += menu[order]['price']


def create_product(order):
    consume_resources(order)
    input(f"\nYour {order} is here. Thank you for your purchase and enjoy. ")
    clr()


def replenish_machine():
    clr()
    show_report()
    print("You replenished the machine with resources.\nThe machine is full again.\n")
    global machine
    machine["water"] = 500
    machine["milk"] = 300
    machine["coffee"] = 100
    show_report()
    input("\nPress any key to use the machine. ")


def main_app():
    clr()
    order = ""

    while order != commands['off']['command']:
        order = ask_for_order()

        if order in menu.keys():

            is_order_possible = check_for_resources(order)
            if is_order_possible is True:

                payment_success = pay_for_order(coins, order)
                if payment_success:
                    create_product(order)
                    reset_coins()
                else:
                    input("\nPress any key to restart coffee machine. ")
                    reset_coins()
                    clr()
            else:
                input("Error: lack of ingredients. Contact the staff. ")
                clr()

        if order == commands['report']['command']:
            clr()
            show_report()
        elif order == commands['replenish']['command']:
            replenish_machine()
            clr()

    clr()
    print("The coffee machine is OFF.\n")


# code

# run program
main_app()
