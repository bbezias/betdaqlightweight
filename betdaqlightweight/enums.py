from enum import Enum


class PriceFormat(Enum):
    """
    The format of a price.

    Decimal: The price is expressed in decimal format – in particular the price is the decimal representation of
    the payout for 1 currency unit stake.
    Fractional: The price is expressed in fractional format – in particular the fraction is the winnings
    for 1 currency unit stake.
    American: The price is expressed in American format – in particular if the price is greater than 0 it means
    the amount of winnings for 100 currency unit stake whereas if the price is less than zero it means the
    amount of currency unit that needs to be staked to win 100 currency units.
    """
    Decimal = 1
    Fractional = 2
    American = 3


class WithdrawRepriceOption(Enum):
    """
    the action to take on a specific Order if a withdrawal occurs on the Market that could cause a
    Rule-4 deduction factor to be applied to the Order (this option only controls what happens to the
    unmatched parts of Orders, those parts that have already been matched will have the rule-4 deduction applied
    regardless of the value of this option).

    Reprice: Reprice the unmatched parts of the Order. It is anticipated that this would be the
    usual option specified by Layers.
    Cancel: Cancel the unmatched parts of the Order.
    DontReprice: Do not reprice the unmatched parts of the Order.
    """
    Reprice = 1
    Cancel = 2
    DontReprice = 3


class OrderKillType(Enum):
    """
    Define how an order is handled when sent to exchange.

    illAndKill: After the initial attempt is made to match this order any unmatched portion of the order is
    immediately cancelled.
    FillOrKill: On the initial attempt to match this order if it is not possible to match a specified amount of
    the order then none of the order will be matched. If it had been possible to match at least the specified amount
    then the amount that can be matched will be matched and the remaining unmatched amount will be cancelled.
    FillOrKillDontCancel: On the initial attempt to match this order if it is not possible to match a specified
    mount of the order then none of the order will be matched. If it had been possible to match at least the specified
    amount then the amount that can be matched will be matched and the remaining unmatched amount will be not be
    cancelled but left as an unmatched order.
    SPIfUnmatched: Same as Normal but any unmatched portion of the order is to be matched at SP when the market
    is turned in-running (or completed).
    """
    Normal = 1
    FillAndKill = 2
    FillOrKill = 3
    FillOrKillDontCancel = 4
    SPIfUnmatched = 5


class Polarity(Enum):
    """
    The side which an order is being sent for.
    """
    back = 1
    lay = 2


class HeartbeatAction(Enum):
    """
    Action to be performed when a threshold period has expired without a Pulse having been received.

    CancelOrders: cancel all unmatched orders.
    SuspendOrders: suspend all unmatched orders.
    SuspendPunter: suspend punter.
    """
    CancelOrders = 1
    SuspendOrders = 2
    SuspendPunter = 3
