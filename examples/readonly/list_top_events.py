from betdaqlightweight.client import Client

c = Client('xxx', 'xxx')
r = c.readonly.list_top_level_events()
print(r)
