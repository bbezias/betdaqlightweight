from betdaqlightweight.client import Client

c = Client('xxx', 'xxx')

r = c.secure.change_heartbeat()

print(r)
