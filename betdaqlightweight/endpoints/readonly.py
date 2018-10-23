from betdaqlightweight.endpoints.base import BaseEndpoint


class Endpoint(BaseEndpoint):

    def list_top_level_events(self, want_play_markets=None):
        """
        Get list of sports and their IDs.

        :param want_play_markets: whether to return play or real markets, None is False
        :return: all sports available
        """
        return self.run('ListTopLevelEvents', 'ListTopLevelEventsRequest', _WantPlayMarkets=want_play_markets)

    def get_event_sub_tree_with_selections(self, event_classifier_ids=None, want_play_markets=None):
        """
        Get the tree of events and markets for given sports/events with selection.

        :param event_classifier_ids: list of sports/events for which to return events/markets
        :param want_play_markets: whether to return play or real markets, None is False
        :return: all markets for the given sport, with comp and event data flattened with selections
        """
        return self.run(
            'GetEventSubTreeWithSelections',
            'GetEventSubTreeWithSelectionsRequest',
            EventClassifierIds=event_classifier_ids,
            _WantPlayMarkets=want_play_markets
        )

    def get_event_sub_tree_no_selections(self, event_classifier_ids=None, want_play_markets=None):
        """
        Get the tree of events and markets for given sports/events with selection.

        :param event_classifier_ids: list of sports/events for which to return events/markets
        :param want_play_markets: whether to return play or real markets, None is False
        :return: all markets for the given sport/event
        """
        return self.run(
            'GetEventSubTreeNoSelections',
            'GetEventSubTreeNoSelectionsRequest',
            EventClassifierIds=event_classifier_ids,
            _WantPlayMarkets=want_play_markets
        )

    def get_market_information(self, market_ids=None):
        """
        Get detailed information about given market(s).

        :param market_ids: market id(s) to get data for.
        :return: market information for each market id provided.
        """
        return self.run(
            'GetMarketInformation',
            'GetMarketInformationRequest',
            MarketIds=market_ids
        )

    def list_market_withdrawal_history(self, market_id=None):
        """
        Get withdrawals from a particular market

        :param market_id: market id to get data for.
        :return: any withdrawals from the market.
        """
        return self.run(
            'ListMarketWithdrawalHistory',
            'ListMarketWithdrawalHistoryRequest',
            _MarketId=market_id
        )

    def get_prices(
            self,
            market_ids=None,
            threshold_amount=0,
            number_for_prices_required=3,
            number_against_prices_required=3,
            want_market_matched_amount=False,
            want_selections_matched_amounts=False,
            want_selection_matched_details=False
    ):
        """
        Get prices by selection for all markets given in market_ids.

        :param market_ids: Filter by a list of event ids
        :param threshold_amount: whether to return play or real markets, None is False
        :param number_for_prices_required: Filter by a list of event ids
        :param number_against_prices_required: Filter by a list of event ids
        :param want_market_matched_amount: Filter by a list of event ids
        :param want_selections_matched_amounts: Filter by a list of event ids
        :param want_selection_matched_details: Filter by a list of event ids

        :return: Prices for each selection in each market.
        """
        return self.run(
            'GetPrices',
            'GetPricesRequest',
            MarketIds=market_ids,
            _ThresholdAmount=threshold_amount,
            _NumberForPricesRequired=number_for_prices_required,
            _NumberAgainstPricesRequired=number_against_prices_required,
            _WantMarketMatchedAmount=want_market_matched_amount,
            _WantSelectionsMatchedAmounts=want_selections_matched_amounts,
            _WantSelectionMatchedDetails=want_selection_matched_details,
        )

    def get_odds_ladder(self, price_format=None):
        """
        Get current odds ladder.

        :param price_format: what odds type to return.
        :return: odds ladder.
        """
        return self.run(
            'GetOddsLadder',
            'GetOddsLadderRequest',
            _PriceFormat=price_format
        )

    def get_list_selections_changed_since(self, selection_sequence_number=0):
        """
        Get withdrawals from a particular market

        :param selection_sequence_number: sequence of the poll to check diffs from.
        :return: any changes to selections since the given sequence number.
        """
        return self.run(
            'ListSelectionsChangedSince',
            'ListSelectionsChangedSinceRequest',
            _SelectionSequenceNumber=selection_sequence_number
        )

    def get_current_selection_sequence_number(self):
        """
        Get the current maximum selectionSequenceNumber.

        :return: max selection sequence number.
        """
        return self.run(
            'GetCurrentSelectionSequenceNumber',
            'GetCurrentSelectionSequenceNumberRequest'
        )

    def list_selection_trades(self, selection_info, currency="GBP"):
        """
        Get the history of trades on the selection(s) specified.

        :param selection_info: list selection info (use filter.selection_info to create).
        :param currency: 3 letter code for currency to return trade info in.
        :return: trades on any selections provided from the tradeId specified.
        """
        return self.run(
            'ListSelectionTrades',
            'ListSelectionTradesRequest',
            selectionRequests=selection_info,
            _currency=currency
        )

    def get_sp_enabled_markets_information(self):
        """
        Get information defining which markets are enabled for starting-price orders.

        :return: information on which markets have SP.
        """
        return self.run(
            'GetSPEnabledMarketsInformation',
            'GetSPEnabledMarketsInformationRequest'
        )
