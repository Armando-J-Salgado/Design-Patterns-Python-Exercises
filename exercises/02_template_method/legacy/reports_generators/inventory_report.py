from .report import Report

class InventoryReport(Report):
    def get_report_type(self):
        return "inventory"
    
    def make_report_rows(self, lines, rows):
        total_units = 0
        low_stock = 0
        for row in rows:
            lines.append(f"{row['sku']} | {row['name']} | {row['units']} units")
            total_units += int(row["units"])
            if int(row["units"]) <= 5:
                low_stock += 1
        lines.append(f"Total units: {total_units}")
        lines.append(f"Low stock: {low_stock}")
        return lines