
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self._customer = customer
        self._coffee = coffee
        self._price = price
        self.all.append(self)

    def get_price(self):
        return self._price

    def set_price(self, price):
        if isinstance(price, int) and 1 <= price <= 10:
            self._price = price
        else:
            raise Exception("Price must be a number 1-10")

    def get_customer(self):
        return self._customer
    
    def set_customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception("Customer must be a Customer type")

    def get_coffee(self):
        return self._coffee

    def set_coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise Exception("Coffee must be a Coffee type")

    price = property(get_price, set_price)
    customer = property(get_customer, set_customer)
    coffee = property(get_coffee, set_coffee)


from .customer import Customer
from .coffee import Coffee
