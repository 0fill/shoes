from controls import *
from models import *
from view import *

catalog = Catalog()
tailor = shoe_maker()

shoe1 = Shoe(sex="male", type="sneakers", color="blue", price=79.99, brand="Nike", size=10)
shoe2 = Shoe(sex="female", type="pumps", color="black", price=199.00, brand="Gucci", size=7)
shoe3 = Shoe(sex="unisex", type="sneakers", color="white", price=59.99, brand="Converse", size=8)
shoe4 = Shoe(sex="male", type="boots", color="brown", price=129.95, brand="Timberland", size=11)
shoe5 = Shoe(sex="female", type="flats", color="pink", price=149.00, brand="Tory Burch", size=6)
shoe6 = Shoe(sex="male", type="dress shoes", color="black", price=249.99, brand="Allen Edmonds", size=9)
shoe7 = Shoe(sex="unisex", type="sneakers", color="grey", price=49.95, brand="Vans", size=7)
shoe8 = Shoe(sex="female", type="sandals", color="gold", price=349.00, brand="Jimmy Choo", size=8)
shoe9 = Shoe(sex="male", type="espadrilles", color="blue", price=39.99, brand="TOMS", size=10)
shoe10 = Shoe(sex="unisex", type="sneakers", color="black and white", price=69.95, brand="Adidas", size=9)

add_shoe(catalog, shoe1)
add_shoe(catalog, shoe2)
add_shoe(catalog, shoe3)
add_shoe(catalog, shoe4)
add_shoe(catalog, shoe5)
add_shoe(catalog, shoe6)
add_shoe(catalog, shoe7)
add_shoe(catalog, shoe8)
add_shoe(catalog, shoe9)
add_shoe(catalog, shoe10)

def run():
    global i
    catalog = Catalog()
    while True:
        main_menu()
        C = False
        while not C:
            i = get_choice(5)
            C = check_choice(i, 5)
        if i == '1':
            catalog_menu()
            C = False
            while not C:
                i = get_choice(5)
                C = check_choice(i, 3)
            if i == '1':
                display(catalog.shoes)
                add_shoe_carts(catalog,)
        elif i == '2':
            add_shoe(catalog,(
                tailor.set_sex(input("please enter sex of shoes"))
                .set_size(input("please enter size of shoes"))
                .set_brand(input("please enter brand of shoes"))
                .set_color(input("please enter color of shoes"))
                .set_price(int(input("please enter price of shoes")))
                .set_type(input("please enter type of shoes"))
            ).create())
        elif i == '3':
            func(remove_shoe,catalog)
            display(catalog.shoes)
            k = chose_shoe(catalog)
            if check_choice(k,len(catalog.shoes)-1):
                remove_shoe(catalog,int(k))


run()
