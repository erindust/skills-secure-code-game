'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal

MAX_ITEM_AMOUNT = Decimal(str(100000)) # maximum price of item in the shop
MAX_QUANTITY = Decimal(str(100)) # maximum quantity of an item in the shop
MIN_QUANTITY = Decimal(str(0)) # minimum quantity of an item in the shop
MAX_TOTAL = Decimal(str(1e6)) # maximum total amount accepted for an order

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    net = Decimal(0)
    expenses = Decimal(0)
    payments = Decimal(0)

    for item in order.items:
        if item.type == 'payment':
            # Sets a reasonable min & max value for the invoice amounts
            if -MAX_ITEM_AMOUNT <= item.amount <= MAX_ITEM_AMOUNT:
                payments += Decimal(str(item.amount))
                net += Decimal(str(item.amount))
        elif item.type == 'product':
            # if Decimal(str(item.amount)) > MAX_ITEM_AMOUNT:
            #     return "Order ID: %s - Item price exceeds maximum amount" % order.id
            # net -= Decimal(str(item.amount)) * Decimal(str(item.quantity))

            if type(item.quantity) is int and MIN_QUANTITY < item.quantity <= MAX_QUANTITY and MIN_QUANTITY < item.amount <= MAX_ITEM_AMOUNT:
                expenses += Decimal(str(item.amount)) * item.quantity
                net -= Decimal(str(item.amount)) * item.quantity
        else:
            return "Invalid item type: %s" % item.type
        print(item)
        print(net)

    if abs(payments) > MAX_TOTAL or expenses > MAX_TOTAL:
        return "Total amount payable for an order exceeded"
    
    if net != Decimal(0):
        if net < 0:
            return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
        else:
            return 'Total amount payable for an order exceeded'
    else:
        return "Order ID: %s - Full payment received!" % order.id
    

# Testing test 8
# The total amount payable in an order should be limited
# num_items = 12
# items = [Item(type='product', description='tv', amount=99999, quantity=num_items)]
# for i in range(num_items):
#     items.append(Item(type='payment', description='invoice_' + str(i), amount=99999, quantity=1))
# order_1 = Order(id='1', items=items)
# print(validorder(order_1))

# # Put payments before products
# items = items[1:] + [items[0]]
# order_2 = Order(id='2', items=items)
# print(validorder(order_2))


#Testing Test 2
# tv_item = Item(type='product', description='tv', amount=1000.00, quantity=1)
# order_2 = Order(id='2', items=[tv_item])
# # self.assertEqual(c.validorder(order_2), 'Order ID: 2 - Payment imbalance: $-1000.00')
# print(validorder(order_2))

#Test 5
service = Item(type='service', description='order shipment', amount=100, quantity=1)
order_1 = Order(id='1', items=[service])
# self.assertEqual(c.validorder(order_1), 'Invalid item type: service')
print(validorder(order_1))  
