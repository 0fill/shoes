import random

from controls import *
from models import *
from view import *

tailor = shoe_maker()
database = get_pickle_file("data/cards.pkl")


def run():
    inventory = get_pickle_file("data/shoes.pkl")

    while True:
        main_menu()
        i = get_choice(3)
        if i == '1':
            catalog_menu()
            i = get_choice(4)
            if i == '1':  #catalog -> cart

                func(add_shoe_carts, inventory)
                #add_shoe_carts(catalog, get_choice(len(catalog.shoes)))
            elif i == '2':  #cart -> catalog
                func(remove_from_cart, inventory)
            elif i == '3':  #check cart
                showtime(inventory.cart)
                must_pay(inventory)
            elif i == '4':  #pay
                pay_menu()
                i = get_choice(2)
                if i == '1':
                    id = get_card()
                    for card in database:
                        if (card.id == id):
                            card_payment(inventory, card)
                elif i == '2':
                    while not check_for_money(inventory, inventory):
                        cash = pay_shoe()
                        if check_cash(cash):
                            cash = int(cash)
                            pay_deposit(inventory, cash)
                    cash_payment(inventory)  #soon
                    pay_massege()

        elif i == '2':
            add_shoe(inventory, (
                tailor.set_sex(input("please enter sex of shoes"))
                .set_size(input("please enter size of shoes"))
                .set_brand(input("please enter brand of shoes"))            #move to controlers later
                .set_color(input("please enter color of shoes"))
                .set_price(int(input("please enter price of shoes")))
                .set_type(input("please enter type of shoes"))
            ).create())
        elif i == '3':
            func(remove_shoe, inventory)
        elif i == '0':
            exit(inventory, database, "data/shoes.pkl", "data/cards.pkl")


run()
