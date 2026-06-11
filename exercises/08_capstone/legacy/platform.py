class CommercePlatform:
    def __init__(self):
        self.orders = {}
        self.listeners = []
        self.next_id = 1

    def add_listener(self, listener):
        if listener not in self.listeners:
            self.listeners.append(listener)

    def _notify(self, event, order):
        payload = {"event": event, "order": order.copy()}
        for listener in list(self.listeners):
            if hasattr(listener, "update"):
                listener.update(payload)
            else:
                listener(payload)

    def create_order(self, customer, items, payment_method="card", delivery="standard"):
        order_id = f"ORD-{self.next_id}"
        self.next_id += 1

        total = 0.0
        for item in items:
            price = float(item["price"]) * int(item.get("quantity", 1))
            kind = item.get("kind", "physical")
            tier = customer.get("tier", "regular")
            if kind == "physical":
                if tier == "gold":
                    price *= 0.90
                elif tier == "silver":
                    price *= 0.95
            elif kind == "digital":
                if payment_method == "invoice":
                    price *= 1.05
            else:
                if tier == "gold":
                    price *= 0.97
            total += price

        if delivery == "express":
            total += 7.5

        if payment_method == "card":
            total += 1.5
        elif payment_method == "invoice":
            total += 3.0

        total = round(total, 2)
        order = {
            "id": order_id,
            "customer": customer["name"],
            "status": "new",
            "total": total,
            "payment_method": payment_method,
            "delivery": delivery,
            "items": [item.copy() for item in items],
        }
        self.orders[order_id] = order
        self._notify("created", order)
        return order

    def pay_order(self, order_id, amount):
        order = self.orders[order_id]
        if order["status"] != "new":
            return False
        if amount < order["total"]:
            return False
        order["status"] = "paid"
        order["paid_amount"] = amount
        self._notify("paid", order)
        return True

    def cancel_order(self, order_id, reason):
        order = self.orders[order_id]
        if order["status"] == "shipped":
            return False
        order["status"] = "cancelled"
        order["reason"] = reason
        self._notify("cancelled", order)
        return True

    def ship_order(self, order_id):
        order = self.orders[order_id]
        if order["status"] != "paid":
            return False
        order["status"] = "shipped"
        self._notify("shipped", order)
        return True

    def invoice(self, order_id, format="plain"):
        order = self.orders[order_id]
        if format == "plain":
            return f"{order['id']}|{order['customer']}|{order['status']}|{order['total']:.2f}"
        if format == "email":
            return f"To {order['customer']}: Your order {order['id']} totals ${order['total']:.2f}"
        return f"Order {order['id']} for {order['customer']} costs {order['total']:.2f}"
