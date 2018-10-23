from betdaqlightweight.client import Client

c = Client('xxx', 'xxx')
r = c.readonly.get_sp_enabled_markets_information()
print(r)
