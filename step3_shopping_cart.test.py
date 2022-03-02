from step3_shopping_cart import Product, ShoppingCart

def test_requirements():
    cart = ShoppingCart()
    doveSoap = Product("Dove Soap", 39.99)
    cart.addProduct(doveSoap, 2)
    axeDeos = Product("Axe Deos", 99.99)
    cart.addProduct(axeDeos, 2)
    cart.setTaxRate(12.5)

    assert cart.contents()[doveSoap] == 2
    assert cart.contents()[axeDeos] == 2
    assert cart.totalTax() == 35.00
    assert cart.totalPrice() == 314.96

def test_negative_price():
    cart = ShoppingCart()
    try:
        doveSoap = Product("Dove Soap", -39.99)
    except:
        return
    assert 0==1, "product should have thrown an exception"

def test_negative_tax():
    cart = ShoppingCart()
    try:
        cart.setTaxRate(-1)
    except:
        return
    assert 0==1, "negative tax rate should have thrown an exception"

def test_negative_product_counts():
    cart = ShoppingCart()
    doveSoap = Product("Dove Soap", 39.99)
    try:
        cart.addProduct(doveSoap, -1)
    except:
        return
    assert 0==1, "negative product count should have thrown an exception"

def main():  
    test_requirements()
    test_negative_price()
    test_negative_tax()
    test_negative_product_counts()

if __name__ == '__main__':    
    main()
    