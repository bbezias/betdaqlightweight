from betdaqlightweight.client import Client
from betdaqlightweight.filters import update_order

c = Client('xxx', 'xxx')

order_1 = update_order(
    bet_id=4910284262,
    delta_stake=4,
    price=500,
    expected_selection_reset_count=0,
    expected_withdrawal_sequence_number=0
)

order_2 = update_order(
    bet_id=4910284261,
    delta_stake=5,
    price=400,
    expected_selection_reset_count=0,
    expected_withdrawal_sequence_number=0
)

r = c.secure.update_orders_no_receipt(orders=[order_1, order_2])

print(r)
