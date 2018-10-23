from betdaqlightweight.client import Client

c = Client('xxx', 'xxx')

r = c.secure.suspend_from_trading()

print(r)
