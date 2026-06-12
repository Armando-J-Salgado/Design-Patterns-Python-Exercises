from .order_state import OrderState

class CancelledStatus(OrderState):
    def valid_transitions(self):
        return []
    
    def transition_to(self, order, new_status, event):
        if (new_status in self.valid_transitions()):
            order.status = new_status
            order.events.append(event)
            return True
        return False