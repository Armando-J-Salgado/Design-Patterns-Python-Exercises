from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "legacy"))

from pricing import calculate_total


def test_student_book_and_food_order():
    items = [
        {"category": "book", "price": 20, "quantity": 1},
        {"category": "food", "price": 10, "quantity": 2},
    ]

    assert calculate_total("student", items) == 36.0


def test_vip_order_gets_multiple_adjustments():
    items = [
        {"category": "book", "price": 40, "quantity": 1},
        {"category": "digital", "price": 50, "quantity": 1},
        {"category": "other", "price": 20, "quantity": 1},
        {"category": "food", "price": 10, "quantity": 1},
    ]

    assert calculate_total("vip", items, rush=True) == 96.56
