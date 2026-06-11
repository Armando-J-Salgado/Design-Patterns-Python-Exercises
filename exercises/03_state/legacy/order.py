class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.status = "draft"
        self.events = []

    def confirm(self):
        if self.status != "draft":
            return False
        self.status = "open"
        self.events.append("confirmed")
        return True

    def pay(self):
        if self.status not in {"draft", "open"}:
            return False
        self.status = "paid"
        self.events.append("paid")
        return True

    def pack(self):
        if self.status != "paid":
            return False
        self.status = "packed"
        self.events.append("packed")
        return True

    def ship(self):
        if self.status != "packed":
            return False
        self.status = "shipped"
        self.events.append("shipped")
        return True

    def cancel(self):
        if self.status == "shipped":
            return False
        self.status = "cancelled"
        self.events.append("cancelled")
        return True
