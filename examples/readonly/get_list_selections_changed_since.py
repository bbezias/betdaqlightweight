from betdaqlightweight.client import Client

c = Client('xxx', 'xxx')
r = c.readonly.get_prices([13614445])
print(r)
