from abc import ABC, abstractmethod

class Category(ABC):
    """Abstract class"""
    @abstractmethod
    def calcular_descuento(self, current_price: float, customer_type: str) -> float:
        pass