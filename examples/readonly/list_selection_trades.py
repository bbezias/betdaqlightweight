from betdaqlightweight.client import Client
from betdaqlightweight.filters import selection_info

c = Client('xxx', 'xxx')
r = c.readonly.list_selection_trades(selection_info(86916630), 'GBP')
print(r)
