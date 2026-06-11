from adjustments.adjustment import Adjustment
from adjustments.amountAdjustment import AmountAdjustment
from adjustments.rushAdjustment import RushAdjustment
from adjustments.vipAdjustment import VipAdjustment

class AdjustmentsApplier():
    def __init__(self, items, rush, customer_type, total):
        self._adjustments = []
        if len(items) >= 4:
            self.suscribe_adjustment(AmountAdjustment())
        if rush:
            self.suscribe_adjustment(RushAdjustment())
        if customer_type == "vip" and total > 100:
            self.suscribe_adjustment(VipAdjustment())
    
    def suscribe_adjustment(self, adjustment: Adjustment):
        self._adjustments.append(adjustment)
    
    def apply_adjustments(self, total):
        new_total = total
        for adjustment in self._adjustments:
            new_total = adjustment.calculate_adjustment(new_total)
        return new_total
            