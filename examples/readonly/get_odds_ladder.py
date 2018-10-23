from betdaqlightweight.client import Client
from betdaqlightweight.enums import PriceFormat

c = Client('xxx', 'xxx')
r = c.readonly.get_odds_ladder(PriceFormat.Fractional.value)
print(r)
