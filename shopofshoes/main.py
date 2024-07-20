from controls import *
from models import *
from view import *

catalog = Catalog()
tailor = shoe_maker()

add_shoe(catalog, Shoe(sex="male", type="sneakers", color="blue", price=79.99, brand="Nike", size=10))
add_shoe(catalog, Shoe(sex="female", type="pumps", color="black", price=199.00, brand="Gucci", size=7))
add_shoe(catalog, Shoe(sex="unisex", type="sneakers", color="white", price=59.99, brand="Converse", size=8))
add_shoe(catalog, Shoe(sex="male", type="boots", color="brown", price=129.95, brand="Timberland", size=11))
add_shoe(catalog, Shoe(sex="female", type="flats", color="pink", price=149.00, brand="Tory Burch", size=6))
add_shoe(catalog, Shoe(sex="male", type="dress shoes", color="black", price=249.99, brand="Allen Edmonds", size=9))
add_shoe(catalog, Shoe(sex="unisex", type="sneakers", color="grey", price=49.95, brand="Vans", size=7))
add_shoe(catalog, Shoe(sex="female", type="sandals", color="gold", price=349.00, brand="Jimmy Choo", size=8))
add_shoe(catalog, Shoe(sex="male", type="espadrilles", color="blue", price=39.99, brand="TOMS", size=10))
add_shoe(catalog, Shoe(sex="unisex", type="sneakers", color="black and white", price=69.95, brand="Adidas", size=9))


def run():
    catalog = Catalog()
    while True:
        main_menu()
        i = get_choice(3)
        if i == '1':
            display(catalog.shoes)
            catalog_menu()
            i = get_choice(4)
            if i == '1':  #catalog -> cart
                func(add_shoe_carts, catalog)
                display(catalog.shoes)
                add_shoe_carts(catalog, get_choice(len(catalog.shoes)))
            elif i == '2':  #cart -> catalog
                func(remove_from_cart, catalog)
            elif i == '3':  #check cart
                display(catalog.cart)
                print(get_prize(catalog))
            elif i == '4':  #pay
                pay_menu()
                i = get_choice(3)
                if i == '1':

        elif i == '2':
            add_shoe(catalog, (
                tailor.set_sex(input("please enter sex of shoes"))
                .set_size(input("please enter size of shoes"))
                .set_brand(input("please enter brand of shoes"))
                .set_color(input("please enter color of shoes"))
                .set_price(int(input("please enter price of shoes")))
                .set_type(input("please enter type of shoes"))
            ).create())
        elif i == '3':
            func(remove_shoe, catalog)


run()
