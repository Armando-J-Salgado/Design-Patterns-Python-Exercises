from category.category import Category

class DigitalCategory(Category):
    def calcular_descuento(self, current_price, customer_type):
        price = current_price
        if customer_type == "vip":
            price *= 0.75
        return price