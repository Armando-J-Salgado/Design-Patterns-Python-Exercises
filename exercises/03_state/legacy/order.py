from statuses.order_state_factory import OrderStateFactory

class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.status = "draft"
        self.events = []
        
    def state(self):
        return OrderStateFactory().set_state(self.status)
        
    def confirm(self):
        return self.state().transition_to(self, "open", "confirmed")

    def pay(self):
        return self.state().transition_to(self, "paid", "paid")

    def pack(self):
        return self.state().transition_to(self, "packed", "packed")

    def ship(self):
        return self.state().transition_to(self, "shipped", "shipped")
        
    def cancel(self):
        return self.state().transition_to(self, "cancelled", "cancelled")
