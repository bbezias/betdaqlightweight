from betdaqlightweight.client import Client

c = Client('xxx', 'xxx')

r = c.secure.cancel_all_orders_on_market([13614307])

print(r)
