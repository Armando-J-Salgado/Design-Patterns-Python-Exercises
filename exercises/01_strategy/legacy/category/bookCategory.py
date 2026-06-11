from category.category import Category

class BookCategory(Category):
    def calcular_descuento(self, current_price, customer_type):
        price = current_price
        
        if customer_type == "student":
            price *= 0.85
        elif customer_type == "vip":
            price *= 0.80
            
        return price