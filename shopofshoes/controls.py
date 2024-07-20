from view import *

def add_shoe(catalog, shoe):
    catalog.shoes.append(shoe)


def add_shoe_carts(catalog, index_of_shoe: int):
    catalog.carts.append(catalog.shoes.pop(index_of_shoe))

def remove_shoe(catalog, index):
    catalog.shoes.pop(index)

def remove_from_cart(catalog, index_of_shoe: int):
    catalog.shoes.append(catalog.cart.pop(index_of_shoe))


def buy_cart(catalog):
    catalog.cart.clear()


def get_prize(catalog):
    return sum(shoe.price for shoe in catalog.shoes)


def check_for_money(catalog, balance):
    return get_prize(catalog) <= balance

def check_choice(index_of_shoe: str,max_choice: int):
    try:
        index_of_shoe = int(index_of_shoe)
    except ValueError:
        return False
    return 0 <= index_of_shoe <= max_choice


def filter_choice(max_choice):
    m = get_input(max_choice)



def alter_prize(shoe, prize):
    shoe.price = prize

def func(func,catalog): #addC removeS removeC
    display(catalog.shoes)
    k = chose_shoe(catalog)
    if check_choice(k,len(catalog.shoes)-1):
        func(catalog,int(k))
