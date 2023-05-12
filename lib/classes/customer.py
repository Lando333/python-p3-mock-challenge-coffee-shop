class Customer:

    all = []

    def __init__(self, name):
        self.set_name(name)
        self.all.append(self)
        
    def orders(self):
        return [order for order in Order.all if order.customer is self]
    
    def coffees(self):
        return set([order.coffee for order in self.orders()])

    def create_order(self, coffee, price):
        if isinstance(coffee, Coffee) and isinstance(price, int):
            Order(self, coffee, price)

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception("Name must be a string between 1 and 15 characters")

    name = property(get_name, set_name)


from .coffee import Coffee
from .order import Order