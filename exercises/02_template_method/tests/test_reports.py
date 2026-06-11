from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "legacy"))

from reports import build_report


def test_sales_report_format():
    rows = [
        {"name": "Alpha", "amount": 10},
        {"name": "Beta", "amount": 15.5},
    ]

    assert build_report("sales", rows) == (
        "Sales Report\n"
        "============\n"
        "Alpha: $10.00\n"
        "Beta: $15.50\n"
        "Total: $25.50\n"
        "Count: 2"
    )


def test_inventory_report_format():
    rows = [
        {"sku": "A1", "name": "Paper", "units": 4},
        {"sku": "B2", "name": "Ink", "units": 9},
    ]

    assert build_report("inventory", rows, title="Warehouse") == (
        "Warehouse\n"
        "=========\n"
        "A1 | Paper | 4 units\n"
        "B2 | Ink | 9 units\n"
        "Total units: 13\n"
        "Low stock: 1"
    )
