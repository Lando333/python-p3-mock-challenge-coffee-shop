#!/usr/bin/env python3
import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

cust1 = Customer("Ryan")

cof1 = Coffee("Americano")
cof2 = Coffee("Esspresso")
cof3 = Coffee("Latte")

o1 = Order(cust1, cof1, 5)
o2 = Order(cust1, cof3, 7)
o3 = Order(cust1, cof2, 5)
o4 = Order(cust1, cof1, 5)
o5 = Order(cust1, cof1, 6)
o6 = Order(cust1, cof1, 6)

ipdb.set_trace()
