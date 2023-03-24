# class Transport :
#     wheels = 4
#
#     def __init__(self, label, color, price, wheels=4):
#         self.label = label
#         self.color = color
#         self.price = price
#         self.wheels = wheels
#
#
# class Car(Transport) :
#     def __init__(self , label , color , price , wheels , drive):
#         super().__init__(label, color, price, wheels)
#         self.drive = drive


class Store:
    def __init__(self, name, ):
        self.name = name

    def getName(self):
        print(self.name)


ATB = Store("ATB")
print(ATB.getName())


class Item:

    def __init__(self, name, description, price):
        self._name = name
        self._desc = description
        self._price = price


class Cart:
    def __init__(self, item):
        self._item = item


class User:
    def __init__(self, name, password, age, card):
        self._name = name
        self._password = password
        self._age = age
        self._card = card


class Admin (User):
    def __init__(self, name, password, age, card, isAdmin):
        super().__init__(name, password, age, card)
        self.isAdmin = isAdmin


class Bag:
    def __init__(self, name):
        self._name = name
