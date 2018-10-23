from betdaqlightweight.client import Client

c = Client('xxx', 'xxx')
r = c.secure.get_account_balances()
print(r)
