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
#
# class AirCraft(Transport) :


class Store:
    def __init__(self, name, ):
        self.name = name


class Cart:
    def __init__(self, name, ):


class User:
    def __init__(self, user_name, user_password, user_age, user_card):
        self.user_name = user_name
        self.user_password = user_password
        self.user_age = user_age
        self.user_card = user_card


class Admin (User):
    def __init__(self, name, ):


class Bag:
