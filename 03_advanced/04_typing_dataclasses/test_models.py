import dataclasses

import pytest

from models import Portfolio, Trade


def test_trade_notional_and_frozen():
    t = Trade("AAPL", 10, 190.0)
    assert t.notional == 1900.0
    with pytest.raises(dataclasses.FrozenInstanceError):
        t.qty = 5


def test_trade_equality_and_repr():
    assert Trade("A", 1, 2.0) == Trade("A", 1, 2.0)
    assert "AAPL" in repr(Trade("AAPL", 1, 1.0))


@pytest.mark.parametrize("qty, price", [(0, 10.0), (5, 0.0), (5, -1.0)])
def test_trade_validation(qty, price):
    with pytest.raises(ValueError):
        Trade("X", qty, price)


def test_portfolio_defaults_are_not_shared():
    a, b = Portfolio(), Portfolio()
    a.add(Trade("A", 1, 1.0))
    assert b.trades == []


def test_portfolio_positions():
    p = Portfolio()
    p.add(Trade("AAPL", 10, 100.0))
    p.add(Trade("MSFT", 5, 200.0))
    p.add(Trade("AAPL", -4, 110.0))
    assert p.position("AAPL") == 6
    assert p.position("MSFT") == 5
    assert p.position("TSLA") == 0
    assert p.symbols() == ["AAPL", "MSFT"]


def test_portfolio_total_notional():
    p = Portfolio()
    p.add(Trade("AAPL", 10, 100.0))
    p.add(Trade("AAPL", -4, 110.0))
    assert p.total_notional() == 1000.0 + (-440.0)
