from betdaqlightweight.client import Client

c = Client('xxx', 'xxx')

r = c.secure.suspend_all_orders()

print(r)
