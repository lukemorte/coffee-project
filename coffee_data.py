commands = {
    "off": {
        "command": "off",
        "help": "Switch the Coffee machine to OFF state."
    },
    "report": {
        "command": "report",
        "help": "List machine's current resources.",
    },
    "replenish": {
        "command": "replenish",
        "help": "Replenish the machine with resources."
    }
}


machine = {
    "water": 500,
    "milk": 300,
    "coffee": 100,
    "money": 0,
}


menu = {
    "espresso": {
        "ingredients": {
            "water": 100,
            "milk": 50,
            "coffee": 15,
        },
        "price": 2.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 30,
        },
        "price": 3.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 150,
            "milk": 100,
            "coffee": 25,
        },
        "price": 3.0,
    },
}
