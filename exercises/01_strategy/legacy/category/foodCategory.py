from category.category import Category

class FoodCategory(Category):
    def calcular_descuento(self, current_price, customer_type):
        price = current_price
        if customer_type == "student":
            price *= 0.95
        elif customer_type == "vip":
            price *= 0.90
        return price