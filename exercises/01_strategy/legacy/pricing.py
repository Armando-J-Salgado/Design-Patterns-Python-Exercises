def calculate_total(customer_type, items, rush=False):
    total = 0.0
    for item in items:
        price = float(item["price"]) * int(item.get("quantity", 1))
        category = item["category"]
        if category == "book":
            if customer_type == "student":
                price *= 0.85
            elif customer_type == "vip":
                price *= 0.80
        elif category == "food":
            if customer_type == "student":
                price *= 0.95
            elif customer_type == "vip":
                price *= 0.90
        elif category == "digital":
            if customer_type == "vip":
                price *= 0.75
        else:
            if customer_type == "student":
                price *= 0.97
            elif customer_type == "vip":
                price *= 0.92
        total += price
    if len(items) >= 4:
        total *= 0.95
    if rush:
        total += 4.5
    if customer_type == "vip" and total > 100:
        total *= 0.97
    return round(total, 2)
