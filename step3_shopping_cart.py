from typing import Dict

class Product:
    def __init__(self, name:str, unitPrice:float):
        assert unitPrice >= 0, "Negative prices are not allowed"
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
        self.__taxRate:float = 0.0

    def setTaxRate(self, rate:float):
        assert rate >= 0, "Negative tax rates are not allowed"
        self.__taxRate = rate / 100.0

    def addProduct(self, product:Product, count:int):
        assert count >= 0, "Negative product count is not allowed"
        if product not in self.__items.keys():
            self.__items[product] = 0
        self.__items[product] += count
        self.__total += product.unitPriceInCents() * count

    def __totalTaxInCents(self):
        return int(round(self.__total * self.__taxRate))

    def totalTax(self):
        return self.__totalTaxInCents() / 100.0
    
    def totalPrice(self):
        return (self.__total + self.__totalTaxInCents()) / 100.0

    def contents(self):
        return self.__items
