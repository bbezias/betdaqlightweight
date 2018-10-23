from betdaqlightweight.client import Client

c = Client('xxx', 'xxx')
r = c.secure.list_orders_changed_since(692)
print(r)
