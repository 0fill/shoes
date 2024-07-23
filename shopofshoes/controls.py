import random
import pickle

from view import *
from models import *


def add_shoe(catalog, shoe):
    catalog.shoes.append(shoe)


def add_balance(catalog, value):
    catalog.balance += value


def add_shoe_carts(catalog, index_of_shoe: int):
    catalog.cart.append(catalog.shoes.pop(index_of_shoe))


def remove_shoe(catalog, index):
    catalog.shoes.pop(index)


def remove_from_cart(catalog, index_of_shoe: int):
    catalog.shoes.append(catalog.cart.pop(index_of_shoe))


def buy_cart(catalog):
    catalog.cart.clear()


def get_prize(catalog):
    return sum(shoe.price for shoe in catalog.cart)


def check_for_money(catalog, money):
    return get_prize(catalog) <= money.balance


def check_choice(index_of_shoe: str, max_choice: int):
    try:
        index_of_shoe = int(index_of_shoe)
    except ValueError:
        return False
    return 0 <= index_of_shoe <= max_choice


def get_choice(max_choice):
    while True:
        m = get_input(max_choice)
        if check_choice(m, max_choice):
            return m


def alter_prize(shoe, prize):
    shoe.price = prize


def func(func1, catalog):  #addC removeS removeC
    showtime(catalog.shoes)
    k = get_choice(len(catalog.shoes) - 1)
    func1(catalog, int(k))


def pay_deposit(catalog, ammount):
    catalog.balance += ammount


def card_payment(catalog, card):
    if check_for_money(catalog, card):
        if random.randint(0, 1):
            card.pay_with(get_prize(catalog))
            buy_cart(catalog)
        else:
            print(">:c")
    else:
        no_money_massege()


def cash_payment(catalog):
    if check_for_money(catalog, catalog):
        catalog.balance -= get_prize(catalog)
        buy_cart(catalog)
        catalog.balance = 0


def check_cash(m: str):
    try:
        m = int(m)
    except:
        error_massege()
        return False
    return True

def get_card(card):
    return card.id

def get_pickle_file(path):
    return pickle.load(open(path, "rb"))

def exit(inventory,cards,inventory_path,cards_path):
    pickle.dump(inventory,open(inventory_path,"wb"))
    pickle.dump(cards,open(cards_path,"wb"))
