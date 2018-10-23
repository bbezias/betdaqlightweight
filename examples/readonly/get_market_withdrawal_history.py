from betdaqlightweight.client import Client

c = Client('xxx', 'xxx')
r = c.readonly.list_market_withdrawal_history(13614445)
print(r)
