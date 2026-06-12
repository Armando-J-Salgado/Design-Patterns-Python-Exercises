from .order_state import OrderState

class OpenStatus(OrderState):
    def valid_transitions(self):
        return ['paid', 'cancelled']