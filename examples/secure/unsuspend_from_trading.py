from betdaqlightweight.client import Client

c = Client('xxx', 'xxx')

r = c.secure.unsuspend_from_trading()

print(r)
