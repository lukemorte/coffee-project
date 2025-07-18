# Coffee Project

from coffee_data import commands
from coffee_data import machine
from coffee_data import menu


# code


def clr():
    print('\n' * 20)


# DONE: 1. program se zeptá: Co si dáte? (espreso, latte, cappucino)
# a) zadej, co chceš vyrobit
# b) tento dotaz by se měl objevit pokaždé, když je akce dokončena (nápoj dokončen,
# nebo pokud např. nebyl dostatek zdrojů)

def ask_for_order():
    options = " / ".join(menu.keys())
    order = input(f"What would you like? ({options}): ")

    allowed = []
    for n in commands:
        allowed.append(commands[n]["command"])

    while order not in menu.keys() and order not in allowed:
        print("Invalid option. Try again:")
        order = input(f"What would you like? ({options}): ")
    return order


# DONE: 2. Vypni program skrytým příkazem "off"


# DONE: 3.Zobraz stav
# a) pokud je zadán příkaz "report", zobrazí se následující report:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5


def show_report():
    print("Current machine's resources:\n")
    for item in machine:
        print(f"{item.capitalize()}: {machine[item]}")

    print("\n")


# TODO: 4. Kontrola, jestli je dostatek zdrojů
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

    print("\n")
    return is_order_possible


# TODO: 5. Proces placení mincemi
# a) pokud je dostatek zdrojů na vybraný nápoj, program požádá o platbu mincemi (kolik quarters, kolik dimes,
# kolik nickles a kolik pennies)
# b) quarter = $0.25, dime = $0.10, nickle = $0.05, penny = $0.01
# c) zkalkuluj mince, které byly vloženy


# TODO: 6. Kontrola, jestli byla transakce úspěšná?
# a) zkontroluj, jestli uživatel vložil dostatek mincí. Např. pokud latte stojí $2.50 a uživatel vložil pouze
# např. $0.52 zahlásí to, že nebyla vložena dostatečná částka a peníze jsou vráceny a vrátí se to zpět na bod 1
# b) pokud uživatel vložil dostatek, do mašiny bude vložena přesná částka za nápoj (tzn. projeví se při příštím
# příkazu report)
# c) pokud uživatel vložil příliš mnoho, stroj vrátí zbytek mincí od největších po nejmenší


# TODO: 7. Vytvoř nápoj
# a) Pokud zdroje na nápoj jsou k dispozici a transakce dopadla dobře, "vytvoří" se nápoj a zdroje se sníží o
# zdroje potřebné k výrobě
# b) jakmile je nápoj hotov, vypiš hlášku, zde je váš ........., užijde si jej.

clr()
order = ""

while order != commands['off']['command']:
    order = ask_for_order()

    if order in menu.keys():
        is_order_possible = check_for_resources(order)

    if order == commands['report']['command']:
        clr()
        show_report()

clr()
print("The coffee machine is OFF.\n")
