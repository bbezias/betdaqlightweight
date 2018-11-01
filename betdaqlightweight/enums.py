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


class MarketStatus(Enum):
    """
    The current status of a market.

    INACTIVE: The Market is not active and has never had any Orders issued against it.
    ACTIVE: The Market it active (that is, Orders can be issued against it).
    SUSPENDED: The Market is not currently active but it has not yet been completed.
    CLOSED: The Market is completed. No further Orders can be issued against the Market but the result of the
    Market is either not yet known or has not yet been entered.
    SETTLED: The Market has been fully settled.
    VOIDED: The Market has been voided. All matched Orders in this Market have also been voided.
    """
    INACTIVE = 1
    ACTIVE = 2
    SUSPENDED = 3
    CLOSED = 4
    SETTLED = 6
    VOIDED = 7


class MarketType(Enum):
    """
    The type of a market.
    """
    Win = 1
    Place = 2
    MatchOdds = 3
    OverUnder = 4
    AsianHandicap = 10
    TwoBall = 11
    ThreeBall = 12
    Unspecified = 13
    MatchMarket = 14
    SetMarket = 15
    Moneyline = 16
    Total = 17
    Handicap = 18
    EachWayNonHandicap = 19
    EachWayHandicap = 20
    EachWayTournament = 21
    RunningBall = 22
    MatchBetting = 23
    MatchBettingInclDraw = 24
    CorrectScore = 25
    HalfTimeFullTime = 26
    TotalGoals = 27
    GoalsScored = 28
    Corners = 29
    OddsOrEvens = 30
    HalfTimeResult = 31
    HalfTimeScore = 32
    MatchOddsExtraTime = 33
    CorrectScoreExtraTime = 34
    OverUnderExtraTime = 35
    ToQualify = 36
    DrawNoBet = 37
    HalftimeAsianHcp = 39
    HalftimeOverUnder = 40
    NextGoal = 41
    FirstGoalscorer = 42
    LastGoalscorer = 43
    PlayerToScore = 44
    FirstHalfHandicap = 45
    FirstHalfTotal = 46
    SetBetting = 47
    GroupBetting = 48
    MatchplaySingle = 49
    MatchplayFourball = 50
    MatchplayFoursome = 51
    TiedMatch = 52
    TopBatsman = 53
    InningsRuns = 54
    TotalTries = 55
    TotalPoints = 56
    FrameBetting = 57
    ToScoreFirst = 58
    ToScoreLast = 59
    FirstScoringPlay = 60
    LastScoringPlay = 61
    HighestScoringQtr = 62
    RunLine = 63
    RoundBetting = 64
    LineBetting = 65


class OrderActionType(Enum):
    """
    The type of an order history audit record.
    """
    Placed = 1
    ExplicitlyUpdated = 2
    Matched = 3
    CancelledExplicitly = 4
    CancelledByReset = 5
    CancelledOnInRunning = 6
    Expired = 7
    MatchedPortionRepricedByR4 = 8
    UnmatchedPortionRepricedByR4 = 9
    UnmatchedPortionCancelledByWithdrawal = 10
    Voided = 11
    Settled = 12
    Suspended = 13
    Unsuspended = 14
    ExpiredByMatching = 15
    Unsettled = 16
    Unmatched = 17
    MatchedPortionRepriced = 18
    CreatedFromLightweightPrice = 19
    CancelledOnComplete = 20


class OrderStatus(Enum):
    """
    The status of an order.

    Unmatched: The order is active and has some amount available for matching (the order may be partially matched).
    Matched: The order has not been settled and it does not have any unmatched amount. Either the order was fully
    matched or it was partially matched and then cancelled.
    Cancelled: This order has been cancelled and at least some of the order was unmatched at the time of
    expiration.
    Settled: The order has been settled.
    Voided: The order has been voided.
    Suspended: At least some of this order is unmatched but the order is suspended and is not available
    for matching.
    """
    Unmatched = 1
    Matched = 2
    Cancelled = 3
    Settled = 4
    Voided = 5
    Suspended = 6


class ReturnCode(Enum):
    """
    Error code coming from Betdaq
    """
    Success = 0
    ResourceError = 1
    SystemError = 2
    EventClassifierDoesNotExist = 5
    MarketDoesNotExist = 8
    SelectionDoesNotExist = 11
    MarketNotActive = 15
    MarketNeitherSuspendedNorActive = 16
    SelectionNotActive = 17
    InsufficientVirtualPunterFunds = 19
    OrderDoesNotExist = 21
    NoUnmatchedAmount = 22
    ResetHasOccurred = 114
    OrderAlreadySuspended = 127
    TradingCurrentlySuspended = 128
    InvalidOdds = 131
    WithdrawalSequenceNumberIsInvalid = 136
    MaximumInputRecordsExceeded = 137
    PunterSuspended = 208
    PunterProhibitedFromPlacingOrders = 240
    InsufficientPunterFunds = 241
    OrderAPIInProgress = 271
    PunterOrderMismatch = 274
    MarketNotEnabledForMultiples = 281
    MultipleLayerParameterAlreadyExists = 285
    LevelsRequestedExceedsMaximum = 288
    NoMultipleOfferAvailable = 289
    InRunningDelayInEffect = 293
    MultipleSelectionsUnderSameEvent = 295
    MultipleSelectionsWithSameName = 296
    DuplicateOrderSpecified = 299
    OrderNotSuspended = 301
    PunterIsSuspendedFromTrading = 302
    PunterHasActiveOrders = 303
    PunterNotSuspendedFromTrading = 304
    ExpiryTimeInThePast = 305
    NoChangeSpecified = 306
    SoapHeaderNotSupplied = 307
    IncorrectVersionNumber = 308
    NoUsernameSpecified = 309
    InvalidParameters = 310
    NoPasswordSpecified = 3011
    MultipleCombinationExclusionAlreadyExists = 312
    MultipleCombinationExlcusionDoesNotExist = 313
    InvalidPassword = 405
    PunterIsBlacklisted = 406
    PunterNotRegisteredAsMultipleLayer = 425
    PunterAlreadyRegisteredForHeartbeat = 462
    PunterNotRegisteredForHeartbeat = 463
    ThresholdSpecifiedTooSmall = 473
    UnmatchedOrderCouldResult = 477
    PunterNotAuthorisedForAPI = 533
    MarketIsForRealMoney = 597
    MarketIsForPlayMoney = 598
    CannotChangeToSPIfUnmatched = 892
