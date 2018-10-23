from betdaqlightweight.client import Client

c = Client('xxx', 'xxx')
r = c.readonly.get_current_selection_sequence_number()
print(r)
