

class Shoe():
    def __init__(self, sex, type, color, price, brand, size):
        self.sex = sex
        self.type = type
        self.color = color
        self.price = price
        self.brand = brand
        self.size = size

    def __str__(self):
        return f'{self.sex} {self.type} {self.color} {self.price} {self.brand} {self.size}'

class Credit_card:
    def __init__(self, id,balance):
        self.id = id
        self.balance = balance

    def add_balance(self, balance):
        self.balance += balance

    def pay_with(self, amount):
        self.balance -= amount


class Catalog():

    def __init__(self):
        self.shoes = []
        self.cart = []
        self.balance = 0


class shoe_maker:
    def __init__(self):
        self.sex = None
        self.type = None
        self.color = None
        self.price = None
        self.brand = None
        self.size = None

    def set_sex(self,sex):
        self.sex = sex
        return self

    def set_type(self,type):
        self.type = type
        return self

    def set_color(self,color):
        self.color = color
        return self

    def set_price(self,price):
        self.price = price
        return self

    def set_brand(self,brand):
        self.brand = brand
        return self

    def set_size(self,size):
        self.size = size
        return self

    def create(self):
        return Shoe(self.sex,self.type,self.color,self.price,self.brand, self.size)