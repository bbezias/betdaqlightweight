from betdaqlightweight.client import Client

c = Client('xxx', 'xxx')

r = c.secure.register_heartbeat()

print(r)
