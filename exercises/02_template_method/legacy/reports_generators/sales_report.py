from .report import Report

class SalesReport(Report):
    def get_report_type(self):
        return 'sales'
    
    def make_report_rows(self, lines, rows) -> list:
        total = 0.0
        for row in rows:
            lines.append(f"{row['name']}: ${row['amount']:.2f}")
            total += float(row["amount"])
        lines.append(f"Total: ${total:.2f}")
        lines.append(f"Count: {len(rows)}")
        return lines