from step1_shopping_cart import Product, ShoppingCart

def main():  
    cart = ShoppingCart()
    doveSoap = Product("Dove Soap", 39.99)
    cart.addProduct(doveSoap, 5)
    assert len(cart.contents()) == 1

    for product, count in cart.contents().items():
        assert product.name() == "Dove Soap"
        assert product.unitPrice() == 39.99
        assert count == 5
    
    assert cart.totalPrice() == 199.95

if __name__ == '__main__':    
    main()
    