from betdaqlightweight.client import Client

c = Client('xxx', 'xxx')

r = c.secure.list_blacklist_information()

print(r)
