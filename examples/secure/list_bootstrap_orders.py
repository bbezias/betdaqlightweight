from betdaqlightweight.client import Client

c = Client('xxx', 'xxx')
r = c.secure.list_bootstrap_orders(0, False)
print(r)
