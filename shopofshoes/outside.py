import pickle, random
from models import *
from controls import *

inventory = Catalog()
add_shoe(inventory, Shoe(sex="male", type="sneakers", color="blue", price=79.99, brand="Nike", size=10))
add_shoe(inventory, Shoe(sex="female", type="pumps", color="black", price=199.00, brand="Gucci", size=7))
add_shoe(inventory, Shoe(sex="unisex", type="sneakers", color="white", price=59.99, brand="Converse", size=8))
add_shoe(inventory, Shoe(sex="male", type="boots", color="brown", price=129.95, brand="Timberland", size=11))
add_shoe(inventory, Shoe(sex="female", type="flats", color="pink", price=149.00, brand="Tory Burch", size=6))
add_shoe(inventory, Shoe(sex="male", type="dress shoes", color="black", price=249.99, brand="Allen Edmonds", size=9))
add_shoe(inventory, Shoe(sex="unisex", type="sneakers", color="grey", price=49.95, brand="Vans", size=7))
add_shoe(inventory, Shoe(sex="female", type="sandals", color="gold", price=349.00, brand="Jimmy Choo", size=8))
add_shoe(inventory, Shoe(sex="male", type="espadrilles", color="blue", price=39.99, brand="TOMS", size=10))
add_shoe(inventory, Shoe(sex="unisex", type="sneakers", color="black and white", price=69.95, brand="Adidas", size=9))

pickle.dump(inventory, open('data/shoes.pkl', 'wb'))

cards = []

for i in range(100):
    cards.append(Credit_card(i,random.randint(20,500)))

pickle.dump(cards, open('data/cards.pkl', 'wb'))