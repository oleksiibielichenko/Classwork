# Abstract class ->
class Auto:
    def __init__(self, label, manufacturer, price, category, wheels=4):
        self._label = label
        self._manufacturer = manufacturer
        self._category = category
        self._price = price
        self._wheels = wheels

    def getCategory(self):
        return self._category


class Sedan (Auto):
    def __init__(self, label, manufacturer, price, category, wheels):
        super().__init__(label, manufacturer, price, category, wheels)

    def fafa(self):
        print("bi-bi")


class Hatchback (Auto):
    def __init__(self, label, manufacturer, price, category, wheels):
        super().__init__(label, manufacturer, price, category, wheels)

    def fafa(self):
        print("meep-meep")


class Truck (Auto):
    def __init__(self, label, manufacturer, price, category, wheels):
        super().__init__(label, manufacturer, price, category, wheels)

    def fafa(self):
        print("fa-fa")


# Single responsibility
class ParkDB:
    _auto = {
        "Sedan": [],
        "Hatchback": [],
        "Truck": [],
    }

    def getProducts(self):
        return self._auto

    def saveProduct(self, auto, category):
        self._auto[category].append(auto)

    def saveProducts(self, auto, category):
        for product in auto:
            self._auto[category].append(auto)

    def editProduct(self):
        pass

    def deleteProduct(self):
        pass


class AutoPark:
    _instance = None

    def __new__(cls, parkDB):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.parkDB = parkDB

        return cls._instance


parkDB = ParkDB()

store = Store(parkDB)

products = store.parkDB.getProducts()

sedan = [
    Sedan("VW", "Germany", "10000$", "Sedan", "18"),
    Sedan("Samsung", "Korea", "1000$", "TV", "22"),
]

hatchback = [
    Hatchback("Sony", "Japan", "140$", "smartphones", "12", True, "2000mAh"),
    Hatchback("LG", "Moldova", "1200$", "smartphones", "21", True, "1200mAh"),
]

truck = [
    Truck("Panasonic", "Canada", "100$", "laptops", "48", True),
    Truck("HP", "Italy", "10230$", "laptops", "21", True),
]


def fill_store(*args):
    for items in args:
        for item in items:
            store.storeDB.saveProduct(item.__dict__, item.getCategory())


fill_store(sedan, hatchback, truck)

print(products['sedan'])
products = storeDB.getProducts()
print(products)


# 1) Create AutoPark
# 2) DB for AutoPark
# 3) Auto
# 4) Sedan , Truck , Hatchback
# 5) Sedan , Truck , Hatchback  : add fafa Method => Sedam => bibi , Truck => fafa , Hatchback => meep-meep
