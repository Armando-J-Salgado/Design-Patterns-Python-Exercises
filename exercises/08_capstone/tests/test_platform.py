from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "legacy"))

from commerce_platform import CommercePlatform


class EventRecorder:
    def __init__(self):
        self.events = []

    def update(self, payload):
        self.events.append(payload)


def test_order_lifecycle_and_notifications():
    shop = CommercePlatform()
    recorder = EventRecorder()
    callback_events = []

    shop.add_listener(recorder)
    shop.add_listener(lambda payload: callback_events.append(payload))

    order = shop.create_order(
        {"name": "Marta", "tier": "gold"},
        [
            {"kind": "physical", "price": 20, "quantity": 2},
            {"kind": "digital", "price": 15, "quantity": 1},
        ],
        payment_method="card",
        delivery="express",
    )

    assert order["id"] == "ORD-1"
    assert order["status"] == "new"
    assert order["total"] == 60.0
    assert recorder.events[0]["event"] == "created"
    assert callback_events[0]["event"] == "created"

    assert shop.pay_order(order["id"], 60.0) is True
    assert shop.ship_order(order["id"]) is True
    assert shop.cancel_order(order["id"], "too late") is False

    assert recorder.events[1]["event"] == "paid"
    assert recorder.events[2]["event"] == "shipped"
    assert shop.invoice(order["id"], format="plain") == "ORD-1|Marta|shipped|60.00"


def test_invoice_formats_and_failed_payment():
    shop = CommercePlatform()
    order = shop.create_order(
        {"name": "Luis", "tier": "regular"},
        [{"kind": "physical", "price": 10, "quantity": 1}],
        payment_method="invoice",
        delivery="standard",
    )

    assert order["total"] == 13.0
    assert shop.pay_order(order["id"], 12.99) is False
    assert shop.invoice(order["id"], format="email") == "To Luis: Your order ORD-1 totals $13.00"
