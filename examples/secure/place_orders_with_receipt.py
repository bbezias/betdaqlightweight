from betdaqlightweight.client import Client
from betdaqlightweight.filters import place_order
from betdaqlightweight import enums
from datetime import datetime, timedelta

c = Client('xxx', 'xxx')

order_1 = place_order(
    selection_id=87629777,
    stake=2,
    price=700,
    polarity=enums.Polarity.back.value,
    expected_selection_reset_count=0,
    expected_withdrawal_sequence_number=0,
    expires_at=datetime.utcnow() + timedelta(days=1)
)

order_2 = place_order(
    selection_id=87629778,
    stake=3,
    price=600,
    polarity=enums.Polarity.back.value,
    expected_selection_reset_count=0,
    expected_withdrawal_sequence_number=0,
    expires_at=datetime.utcnow() + timedelta(days=1)
)

r = c.secure.place_orders_with_receipt(orders=[order_1, order_2])

print(r)
