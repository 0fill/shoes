from controls import *


def display(shoes: list):
    for shoe in enumerate(shoes):
        print(f"{shoe[0]}.{shoe[1]}")


def chose_shoe(catalog):
    i = input(f"which shoe you want(from 0 to {len(catalog.shoes) - 1}): ")
    if check_choice(0, len(catalog.shoes) - 1):
        return i


def get_input(index):
    return input(f"please choose an action(0-{index}): ")


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
