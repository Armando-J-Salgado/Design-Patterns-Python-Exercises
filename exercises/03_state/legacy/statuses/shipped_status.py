from .order_state import OrderState

class ShippedStatus(OrderState):
    def valid_transitions(self):
        return []