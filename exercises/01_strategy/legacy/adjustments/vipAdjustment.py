from adjustments.adjustment import Adjustment

class VipAdjustment(Adjustment):
    def calculate_adjustment(self, total):
        return total * 0.97