from betdaqlightweight.client import Client

c = Client('xxx', 'xxx')

r = c.secure.suspend_orders([111111])

print(r)
