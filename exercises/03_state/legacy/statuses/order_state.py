from abc import ABC, abstractmethod

class OrderState(ABC):
        
    @abstractmethod
    def valid_transitions(self) -> list:
        pass    
    
    def transition_to(self, order, new_status, event):
        if (new_status in self.valid_transitions()):
            order.status = new_status
            order.events.append(event)
            return True
        return False
    
