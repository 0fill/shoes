from controls import *


def showtime(shoes: list):
    for shoe in enumerate(shoes):
        print(f"{shoe[0]}.{shoe[1]}")


def get_input(index):
    return input(f"please choose (0-{index}): ")


#def card_payment():
#   print("insert card")
#  if check_for_money(catalog_menu(),card):
#     if random.randint(0, 1):
#        print("payed succesfully")
#   else:
#      print("not payed")

def get_card():
    b = input("enter id of card: ")
    return b


def main_menu():
    print(f"""
----------MAIN MENU----------
|     1 - browse catalog    |
|     2 - add shoe          |
|     3 - remove shoe       |
|     4 - exit              |
-----------------------------
""")


def catalog_menu():
    print(f"""1- add to cart
2- remove from cart
3- check the cart
4- pay""")


def pay_menu():
    print(f"1-card\n2-cash")


def pay_shoe():
    return  input("please chose vlue you want to deposit: ")


def error_massege():
    print("please enter a correct attribute")


def pay_massege():
    print("thank you for your purchase")

def must_pay(V):
    print(get_prize(V))

def no_money_massege():
    print("youre broke")
