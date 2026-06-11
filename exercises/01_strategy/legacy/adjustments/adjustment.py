from abc import ABC, abstractmethod

class Adjustment(ABC):
    @abstractmethod
    def calculate_adjustment(self, total) -> float:
        pass