from abc import ABC, abstractmethod

class Report(ABC):
    
    @abstractmethod
    def get_report_type(self) -> str:
        pass
    
    @abstractmethod
    def make_report_rows(self, lines: list, rows) -> list:
        pass 
    
    def generate_report(self, rows, title):
        title = title or f"{self.get_report_type().title()} Report"
        lines = [title, "=" * len(title)]
        
        lines = self.make_report_rows(lines, rows)
        
        return "\n".join(lines)
        
        