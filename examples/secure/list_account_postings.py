from betdaqlightweight.client import Client
from datetime import datetime

c = Client('xxx', 'xxx')
r = c.secure.list_account_postings(datetime(year=2016, month=1, day=1), datetime.utcnow())
print(r)
