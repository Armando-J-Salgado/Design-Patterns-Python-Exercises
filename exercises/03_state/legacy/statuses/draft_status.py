from .order_state import OrderState

class DraftStatus(OrderState):
    
    def valid_transitions(self) -> list:
        return ['open', 'paid', 'cancelled']