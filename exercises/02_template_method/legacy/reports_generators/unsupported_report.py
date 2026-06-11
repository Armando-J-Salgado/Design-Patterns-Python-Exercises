from .report import Report

class UnsupportedReport(Report):
    def get_report_type(self):
        return "Unsupported report"
    
    def make_report_rows(self, lines, rows):
        lines.append("Unsupported report")
        return lines