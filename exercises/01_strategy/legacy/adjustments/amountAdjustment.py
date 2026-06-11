from adjustments.adjustment import Adjustment

class AmountAdjustment(Adjustment):
    def calculate_adjustment(self, total):
        return total * 0.95 