from betdaqlightweight.client import Client

c = Client('xxx', 'xxx')

r = c.secure.unsuspend_orders([111111])

print(r)
