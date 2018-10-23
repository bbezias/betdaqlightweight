from betdaqlightweight.client import Client
from betdaqlightweight.filters import place_order
from betdaqlightweight import enums
from datetime import datetime, timedelta

c = Client('xxx', 'xxx')

order_1 = place_order(
    selection_id=86916201,
    stake=2,
    price=1000,
    polarity=enums.Polarity.back.value,
    expected_selection_reset_count=0,
    expected_withdrawal_sequence_number=0,
    expires_at=datetime.utcnow() + timedelta(days=1)
)

order_2 = place_order(
    selection_id=86916201,
    stake=2,
    price=900,
    polarity=enums.Polarity.back.value,
    expected_selection_reset_count=0,
    expected_withdrawal_sequence_number=0,
    expires_at=datetime.utcnow() + timedelta(days=1)
)

r = c.secure.place_orders_no_receipt(orders=[order_1, order_2], want_all_or_nothing_behaviour=True)

print(r)
