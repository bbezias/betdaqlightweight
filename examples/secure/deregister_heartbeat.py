from betdaqlightweight.client import Client

c = Client('xxx', 'xxx')

r = c.secure.deregister_heartbeat()

print(r)
