from adjustments.adjustment import Adjustment

class RushAdjustment(Adjustment):
    def calculate_adjustment(self, total):
        return total + 4.5