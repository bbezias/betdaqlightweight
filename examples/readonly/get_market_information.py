from betdaqlightweight.client import Client

c = Client('xxx', 'xxx')
r = c.readonly.get_list_selections_changed_since(0)
print(r)
