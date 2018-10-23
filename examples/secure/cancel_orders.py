from betdaqlightweight.client import Client

c = Client('xxx', 'xxx')

r = c.secure.cancel_orders(order_ids=[4910282756])

print(r)
