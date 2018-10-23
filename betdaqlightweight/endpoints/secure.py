from betdaqlightweight.endpoints.base import BaseEndpoint
from betdaqlightweight import enums


class Endpoint(BaseEndpoint):

    def get_account_balances(self):
        """
        Get summary of current balances.

        :return: account information for logged in user.
        :rtype: dict
        """
        return self.run('GetAccountBalances', 'GetAccountBalancesRequest')

    def list_account_postings(self, start_time, end_time):
        """
        Get account transactions between two given date and times.

        :param start_time: earlier time to include transactions from.
        :type start_time: datetime.datetime
        :param end_time: latest time to include transactions until.
        :type end_time: datetime.datetime
        :return: account transactions over the specified period.
        """
        return self.run(
            'ListAccountPostings',
            'ListAccountPostingsRequest',
            _StartTime=start_time,
            _EndTime=end_time
        )

    def list_account_postings_by_id(self, transaction_id):
        """
        Get account transactions with transaction_id specified.

        :param transaction_id: lower cutoff for transactionIds to include.
        :type transaction_id: int
        :return: account transactions greater than specified transaction_id.
        """
        return self.run(
            'ListAccountPostingsById',
            'ListAccountPostingsByIdRequest',
            _TransactionId=transaction_id
        )

    def change_password(self, password):
        """
        Change the password for the logged in user.

        :param password: new password to be used for logged in user.
        :type password: str
        :return: None
        """
        return self.run(
            'ChangePassword',
            'ChangePasswordRequest',
            _Password=password
        )

    def list_bootstrap_orders(self, sequence_number, want_settled_orders_on_unsettled_markets=False):
        """
        Get the initial list of orders that's need to be taken into consideration when establishing positions.
        Information about the following orders will be returned:
            •	active orders
            •	fully matched orders
            •	cancelled orders that have a matched portion
            •	suspended orders
            •	some settled or voided orders under some conditions

        :param sequence_number: lower bound cutoff for sequence updates to include,
                               -1 will set to earliest possible sequence.
        :type sequence_number: int
        :param want_settled_orders_on_unsettled_markets: Flag indicating whether or not information about settled orders
                                                    on unsettled markets should be returned.
        :type want_settled_orders_on_unsettled_markets: bool
        :return: orders that have changed.
        """
        return self.run(
            'ListBootstrapOrders',
            'ListBootstrapOrdersRequest',
            SequenceNumber=sequence_number,
            wantSettledOrdersOnUnsettledMarkets=want_settled_orders_on_unsettled_markets
        )

    def list_orders_changed_since(self, sequence_number):
        """
        Get a list of orders for the logged in user that have changed since a given sequence number.
        Utilised to maintain position information after initial position is established with list_orders.

        :param sequence_number: lower bound cutoff for sequence updates to include.
        :type sequence_number: int
        :return: orders that have changed.
        """
        return self.run(
            'ListOrdersChangedSince',
            'ListOrdersChangedSinceRequest',
            SequenceNumber=sequence_number
        )

    def get_order_details(self, order_id):
        """
        Get detailed information about an order.
        This API returns full detail and history about an order. This API should not be called routingly
        but only in the exceptional case where there is some query or uncertainity about
        the status of a particular order.

        :param order_id: id of the order we wish to get history for.
        :type order_id: int
        :return: single orders history and current status.
        """
        return self.run(
            'GetOrderDetails',
            'GetOrderDetailsRequest',
            _OrderId=order_id
        )

    def place_orders_no_receipt(self, want_all_or_nothing_behaviour, orders):
        """
        Places one or more orders at exchange.
        Receipt determines whether to wait for complete matching cycle or just return the order ID.

        :param orders: List of orders to be sent to exchange
        :type orders: list of betdaq_py.filters.create_order
        :param want_all_or_nothing_behaviour: defines whether to kill all orders on any error or place orders
         independently.
        :type want_all_or_nothing_behaviour: bool
        :return: Order ID.
        """
        return self.run(
            'PlaceOrdersNoReceipt',
            'PlaceOrdersNoReceiptRequest',
            WantAllOrNothingBehaviour=want_all_or_nothing_behaviour,
            Orders={'Order': orders}
        )

    def place_orders_with_receipt(self, orders):
        """
        Places one or more orders at exchange.
        Receipt determines whether to wait for complete matching cycle or just return the order ID.

        :param orders: List of orders to be sent to exchange
        :type orders: list of betdaq_py.filters.create_order

        :return: Order details.
        """
        return self.run(
            'PlaceOrdersWithReceipt',
            'PlaceOrdersWithReceiptRequest',
            Orders={'Order': orders}
        )

    def update_orders_no_receipt(self, orders):
        """
        Update orders on exchange

        :param orders: list of order updates to be sent to exchange.
        :type orders: list of betdaq_py.filters.update_order

        :return: bet id and status of update.
        """
        return self.run(
            'UpdateOrdersNoReceipt',
            'UpdateOrdersNoReceiptRequest',
            Orders=[{'Order': orders}]
        )

    def cancel_orders(self, order_ids):
        """
        Cancel one or more orders on exchange

        :param order_ids: list of order ids to be cancelled.
        :type order_ids: list of ints
        :return: information on the cancellation status of each order.
        """
        return self.run(
            'CancelOrders',
            'CancelOrdersRequest',
            OrderHandle=order_ids
        )

    def cancel_all_orders_on_market(self, market_ids):
        """
        Cancel all orders on one or more markets on exchange

        :param market_ids: list of market ids to be cancelled.
        :type market_ids: list of ints
        :return: information on the cancellation status of each order.
        """
        return self.run(
            'CancelAllOrdersOnMarket',
            'CancelAllOrdersOnMarketRequest',
            MarketIds=market_ids
        )

    def cancel_all_orders(self):
        """
        Cancels all unmatched orders across all markets.

        :return: information on the cancellation status of each order.
        """
        return self.run(
            'CancelAllOrders',
            'CancelAllOrdersRequest'
        )

    def list_blacklist_information(self):
        """
        Lists the black-list status for the punter.

        :return: list of every API from which the Punter is currentltly black-listed along with the remaining time
                 (in milli-seconds) of the black-list period for that API.
        """
        return self.run(
            'ListBlacklistInformation',
            'ListBlacklistInformationRequest'
        )

    def suspend_from_trading(self):
        """
        Suspend any of your orders from being matched. For emergency use only.

        :return: response of request success.
        """
        return self.run(
            'SuspendFromTrading',
            'SuspendFromTradingRequest'
        )

    def unsuspend_from_trading(self):
        """
        Reverse the suspension of trading. All active orders must be cancelled or suspended before you can unsuspend.

        :return: response of request success.
        """
        return self.run(
            'UnsuspendFromTrading',
            'UnsuspendFromTradingRequest'
        )

    def suspend_orders(self, order_ids):
        """
        Suspend one or more orders on exchange

        :param order_ids: list of order ids to be suspended.
        :type order_ids: list of ints
        :return: information on the suspension status of each order.
        """
        return self.run(
            'SuspendOrders',
            'SuspendOrdersRequest',
            OrderIds=order_ids
        )

    def suspend_all_orders_on_market(self, market_id):
        """
        Suspend all orders on a given market.

        :param market_id: market id to be suspend orders on.
        :type market_id: int
        :return: information on the suspension status of each order.
        """
        return self.run(
            'SuspendAllOrdersOnMarket',
            'SuspendAllOrdersOnMarketRequest',
            _MarketId=market_id
        )

    def suspend_all_orders(self):
        """
        Suspend all orders.

        :return: information on the suspension status of each order.
        """
        return self.run(
            'SuspendAllOrders',
            'SuspendAllOrdersRequest'
        )

    def unsuspend_orders(self, order_ids):
        """
        Unsuspends one or more suspended orders.

        :param order_ids: list of order ids to unsuspend.
        :type order_ids: list
        :return:
        """
        return self.run(
            'UnsuspendOrders',
            'UnsuspendOrdersRequest',
            OrderIds=order_ids
        )

    def register_heartbeat(self, threshold_ms=6000, heartbeat_action=enums.HeartbeatAction.CancelOrders.value):
        """
        Register the Punter as requiring a Heartbeat. Must send a Pulse < every ThresholdMs to stay alive.

        :param heartbeat_action: The action that should be taken if a Pulse is not received within the threshold.
        :type heartbeat_action: betdaqlightweight.enums.HeartbeatAction
        :param threshold_ms: The maximum period (in milli-seconds) that can elapse between Pulse API calls being
                            received before the system takes the relevant action.
        :type threshold_ms: int
        :return: response of request success.
        """
        return self.run(
            'RegisterHeartbeat',
            'RegisterHeartbeatRequest',
            _ThresholdMs=threshold_ms,
            _HeartbeatAction=heartbeat_action
        )

    def change_heartbeat(self, threshold_ms=6000, heartbeat_action=enums.HeartbeatAction.CancelOrders.value):
        """
        Update the parameter of Heartbeat.

        :param heartbeat_action: The action that should be taken if a Pulse is not received within the threshold.
        :type heartbeat_action: betdaq_py.enums.HeartbeatAction
        :param threshold_ms: The maximum period (in milli-seconds) that can elapse between Pulse API calls being
                            received before the system takes the relevant action.
        :return: response of request success.
        """
        return self.run(
            'ChangeHeartbeatRegistration',
            'ChangeHeartbeatRegistrationRequest',
            _ThresholdMs=threshold_ms,
            _HeartbeatAction=heartbeat_action
        )

    def deregister_heartbeat(self):
        """
        Deregister the Punter as requiring a Heartbeat.

        :return: response of request success.
        """
        return self.run(
            'DeregisterHeartbeat',
            'DeregisterHeartbeatRequest'
        )

    def pulse(self):
        """
        Notify the system that the application is still active and still has connectivity.

        :return: Time of pulse performance.
        """
        return self.run(
            'Pulse',
            'PulseRequest'
        )
