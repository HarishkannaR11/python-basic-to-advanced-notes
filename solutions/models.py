from dataclasses import dataclass, field


@dataclass(frozen=True)
class Trade:
    symbol: str
    qty: int
    price: float

    def __post_init__(self):
        if self.qty == 0:
            raise ValueError("qty must be non-zero")
        if self.price <= 0:
            raise ValueError("price must be positive")

    @property
    def notional(self) -> float:
        return self.qty * self.price


@dataclass
class Portfolio:
    trades: list[Trade] = field(default_factory=list)

    def add(self, trade: Trade) -> None:
        self.trades.append(trade)

    def position(self, symbol: str) -> int:
        return sum(t.qty for t in self.trades if t.symbol == symbol)

    def total_notional(self) -> float:
        return sum(t.notional for t in self.trades)

    def symbols(self) -> list[str]:
        return sorted({t.symbol for t in self.trades})
