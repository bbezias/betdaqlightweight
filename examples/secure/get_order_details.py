from betdaqlightweight.client import Client

c = Client('xxx', 'xxx')
r = c.secure.get_order_details(408582492)
print(r)
