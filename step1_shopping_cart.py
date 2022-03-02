from typing import Dict

class Product:
    def __init__(self, name:str, unitPrice:float):
        self.__name = name
        self.__unitPrice = int(unitPrice * 100)

    def name(self):
        return self.__name
    
    def unitPrice(self):
        return self.__unitPrice / 100.0

    def unitPriceInCents(self):
        return self.__unitPrice

class ShoppingCart:
    def __init__(self):
        self.__items:Dict[Product, int] = {}
        self.__total:int = 0

    def addProduct(self, product:Product, count:int):
        if product not in self.__items.keys():
            self.__items[product] = 0
        self.__items[product] += count
        self.__total += product.unitPriceInCents() * count
    
    def totalPrice(self):
        return self.__total / 100.0

    def contents(self):
        return self.__items
