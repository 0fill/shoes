from controls import *
import random

def display(shoes: list):
    for shoe in enumerate(shoes):
        print(f"{shoe[0]}.{shoe[1]}")


def chose_shoe(catalog):
    while True:
        i = input(f"which shoe you want(from 0 to {len(catalog.shoes) - 1}): ")
        if check_choice(0, len(catalog.shoes) - 1):
            return i


def get_input(index):
    return input(f"please choose (0-{index}): ")

def card_payment():
    print("insert card")
    if
    if random.randint(0, 1)
        print("payed succesfully")
    else:
        print("not payed")

def main_menu():
    print(f"""
----------MAIN MENU----------
|     1 - browse catalog    |
|     2 - add shoe          |
|     3 - remove shoe       |
-----------------------------
""")


def catalog_menu():
    print(f"""1- add to cart
2- remove from cart
3- check the cart
4- pay""")

def pay_menu():
    print(f"""1-card
2-cash
3-check""")

