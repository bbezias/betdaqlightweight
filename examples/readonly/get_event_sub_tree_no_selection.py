from betdaqlightweight.client import Client

c = Client('xxx', 'xxx')
r = c.readonly.get_event_sub_tree_no_selections([5402241])
print(r)
