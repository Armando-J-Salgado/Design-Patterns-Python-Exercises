from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "legacy"))

from order import Order


def test_order_moves_through_valid_states():
    order = Order("A-1")

    assert order.confirm() is True
    assert order.pay() is True
    assert order.pack() is True
    assert order.ship() is True
    assert order.status == "shipped"
    assert order.events == ["confirmed", "paid", "packed", "shipped"]


def test_invalid_transition_is_rejected():
    order = Order("A-2")

    assert order.ship() is False
    assert order.status == "draft"
    assert order.cancel() is True
    assert order.pay() is False
