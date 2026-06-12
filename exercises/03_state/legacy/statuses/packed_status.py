from .order_state import OrderState

class PackedStatus(OrderState):
    def valid_transitions(self):
        return ['shipped', 'cancelled']