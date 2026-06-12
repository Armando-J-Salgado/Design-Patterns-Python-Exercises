from .order_state import OrderState

class PaidStatus(OrderState):
    def valid_transitions(self):
        return ['packed', 'cancelled']