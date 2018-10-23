from betdaqlightweight.client import Client

c = Client('xxx', 'xxx')

r = c.secure.cancel_all_orders()

print(r)
