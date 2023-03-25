# Singleton pattern
# SOLID

# Abstract class ->
class Device:
    def __init__(self, label, manufacturer, price, category):
        self._label = label
        self._manufacturer = manufacturer
        self._category = category
        self._price = price

    def getCategory(self):
        return self._category


class TV (Device):
    def __init__(self, label, manufacturer, price, category, screen):
        super().__init__(label, manufacturer, price, category)
        self._screen = screen


class Laptop (Device):
    def __init__(self, label, manufacturer, price, category, screen, rgb):
        super().__init__(label, manufacturer, price, category)
        self._screen = screen
        self._rgb = rgb


class Smartphone (Device):
    def __init__(self, label, manufacturer, price, category, screen, rgb, accumulator):
        super().__init__(label, manufacturer, price, category)
        self._screen = screen
        self._rgb = rgb
        self._accumulator = accumulator


# Single responsibility
class StoreDB:
    _products = {
        "laptops": [],
        "smartphones": [],
        "TV": []
    }

    def getProducts(self):
        return self._products

    def saveProduct(self, product, category):
        self._products[category].append(product)

    def saveProducts(self, products, category):
        for product in products:
            self._products[category].append(product)

    def editProduct(self):
        pass

    def deleteProduct(self):
        pass


class Store:
    _instance = None

    def __new__(cls, storeDB):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.storeDB = storeDB

        return cls._instance


storeDB = StoreDB()

store = Store(storeDB)

products = store.storeDB.getProducts()

TV = [
    TV("LG", "Germany", "100$", "TV", "18"),
    TV("Samsung", "Korea", "1000$", "TV", "22"),
]

Smartphones = [
    Smartphone("Sony", "Japan", "140$", "smartphones", "12", True, "2000mAh"),
    Smartphone("LG", "Moldova", "1200$", "smartphones", "21", True, "1200mAh"),
]

Laptops = [
    Laptop("Panasonic", "Canada", "100$", "laptops", "48", True),
    Laptop("HP", "Italy", "10230$", "laptops", "21", True),
]


def fill_store(*args):
    for items in args:
        for item in items:
            store.storeDB.saveProduct(item.__dict__, item.getCategory())


fill_store(TV, Smartphones, Laptops)

print(products['laptops'])
products = storeDB.getProducts()
print(products)


# 1) Create AutoPark
# 2) DB for AutoPark
# 3) Auto
# 4) Sedan , Truck , Hatchback
# 5) Sedan , Truck , Hatchback  : add fafa Method => Sedam => bibi , Truck => fafa , Hatchback => meep-meep
