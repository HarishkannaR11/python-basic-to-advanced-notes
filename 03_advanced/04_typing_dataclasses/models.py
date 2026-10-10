from dataclasses import dataclass, field


@dataclass(frozen=True)
class Trade:
    """One trade. Immutable.

    Fields: `symbol: str`, `qty: int`, `price: float` (add them below).
    - property `notional` -> qty * price
    - raise ValueError (in __post_init__) if qty == 0 or price <= 0
    """

    @property
    def notional(self) -> float:
        raise NotImplementedError


@dataclass
class Portfolio:
    """A collection of trades.

    - field `trades`: a list of Trade, empty by default (use default_factory).
    - `add(trade)` appends a trade.
    - `position(symbol) -> int` net quantity for that symbol (buys +, sells -).
    - `total_notional() -> float` sum of notional over all trades.
    - `symbols() -> list[str]` sorted unique symbols.
    """

    def add(self, trade) -> None:
        raise NotImplementedError

    def position(self, symbol: str) -> int:
        raise NotImplementedError

    def total_notional(self) -> float:
        raise NotImplementedError

    def symbols(self) -> list[str]:
        raise NotImplementedError
