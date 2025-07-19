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


# DONE: 1. program se zeptá: Co si dáte? (espreso, latte, cappucino)
# a) zadej, co chceš vyrobit
# b) tento dotaz by se měl objevit pokaždé, když je akce dokončena (nápoj dokončen,
# nebo pokud např. nebyl dostatek zdrojů)

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


# DONE: 2. Vypni program skrytým příkazem "off"


# DONE: 3. Zobraz stav
# a) pokud je zadán příkaz "report", zobrazí se následující report:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5


def show_report():
    print("Current machine's resources:\n")
    for item in machine:
        value = machine[item]
        if item == "money":
            print(f"{item.capitalize()}: ${value:.2f}")
        else:
            print(f"{item.capitalize()}: {value}")

    print("\n")


# DONE: 4. Kontrola, jestli je dostatek zdrojů
# a) když si uživatel vybere nápoj, program zjistí, jestli je dostatek zdrojů
# b) pokud např. latte potřebuje 200ml vody a je k dispozici jen 100ml, tak to musí zahlásit, že není dostatek vody
# c) to samé nastane u ostatních zdrojů.
# d) pokud není dostatek zdrojů, vrací se na bod 1


def check_for_resources(order):
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


# DONE: 5. Proces placení mincemi
# a) pokud je dostatek zdrojů na vybraný nápoj, program požádá o platbu mincemi (kolik quarters, kolik dimes,
# kolik nickles a kolik pennies)
# b) quarter = $0.25, dime = $0.10, nickle = $0.05, penny = $0.01
# c) zkalkuluj mince, které byly vloženy


def get_input_number(s):
    while True:
        n = input(s)
        try:
            n = int(n)
            break
        except ValueError:
            print("Not a number, try again.")
    return n


def get_coins_number(coins):
    return coins["quarters"] * 0.25 + coins["dimes"] * 0.10 + coins["nickles"] * 0.05 + coins["pennies"] * 0.01


def show_current_coins(coins):
    print(f"Inserted: ${get_coins_number(coins):.2f}")


def get_remain_coins(coins, p_price):
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


# DONE: 6. Kontrola, jestli byla transakce úspěšná?
# a) zkontroluj, jestli uživatel vložil dostatek mincí. Např. pokud latte stojí $2.50 a uživatel vložil pouze
# např. $0.52 zahlásí to, že nebyla vložena dostatečná částka a peníze jsou vráceny a vrátí se to zpět na bod 1
# b) pokud uživatel vložil dostatek, do mašiny bude vložena přesná částka za nápoj (tzn. projeví se při příštím
# příkazu report)
# c) pokud uživatel vložil příliš mnoho, stroj vrátí zbytek mincí od největších po nejmenší


# DONE: 7. Vytvoř nápoj
# a) Pokud zdroje na nápoj jsou k dispozici a transakce dopadla dobře, "vytvoří" se nápoj a zdroje se sníží o
# zdroje potřebné k výrobě
# b) jakmile je nápoj hotov, vypiš hlášku, zde je váš ........., užijde si jej.

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


main_app()