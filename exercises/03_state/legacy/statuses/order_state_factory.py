from .draft_status import DraftStatus
from .order_state import OrderState
from .open_status import OpenStatus
from .packed_status import PackedStatus
from .paid_status import PaidStatus
from .shipped_status import ShippedStatus
from .cancelled_status import CancelledStatus

class OrderStateFactory():
    def set_state(self, state):
        match(state):
            case 'draft':
                return DraftStatus()
            case 'open':
                return OpenStatus()
            case 'paid':
                return PaidStatus()
            case 'packed':
                return PackedStatus()
            case 'shipped':
                return ShippedStatus()
            case 'cancelled':
                return CancelledStatus()
            case _:
                raise Exception('Invalid status')