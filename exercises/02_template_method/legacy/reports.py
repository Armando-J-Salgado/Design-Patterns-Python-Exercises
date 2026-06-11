from reports_generators.inventory_report import InventoryReport
from reports_generators.sales_report import SalesReport
from reports_generators.unsupported_report import UnsupportedReport

def build_report(report_type, rows, title=None):
    report = None
    match (report_type):
        case "sales":
            report = SalesReport()
        case "inventory":
            report = InventoryReport()           
        case _:
            report = UnsupportedReport()
    
    return report.generate_report(rows, title)


