from betdaqlightweight.client import Client

c = Client('xxx', 'xxx')
r = c.secure.list_account_postings_by_id(408582492)
print(r)
