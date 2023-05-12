class Coffee:

    all = []

    def __init__(self, name):
        self.set_name(name)     # name must be initialized with object
        self.all.append(self)

    def orders(self):
        return [order for order in Order.all if order.coffee is self]

    def customers(self):
        return list(set([ order.customer for order in self.orders() ]))

    def num_orders(self):
        return len(Coffee.orders(self))

    def average_price(self):
        return mean([order.price for order in self.orders()])

    def get_name(self):
        return self._name

    def set_name(self, name):
        if not hasattr(self, "_name"):
            self._name = name
        else:
            raise Exception("Cannot be renamed after creation")

    name = property(get_name, set_name)



from .order import Order
from .customer import Customer
from statistics import mean