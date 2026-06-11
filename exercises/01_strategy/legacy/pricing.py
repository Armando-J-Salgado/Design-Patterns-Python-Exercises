from category.categoryFactory import CategoryFactory
from adjustments.adjustmentsApplier import AdjustmentsApplier

def calculate_total(customer_type, items, rush=False):
    total = 0.0
    
    for item in items:
        price = float(item["price"]) * int(item.get("quantity", 1))
        category = item["category"]
        #Se agrega un factory para mantener OCP y SRP
        strategy = CategoryFactory().generate_category(category);
        total += strategy.calcular_descuento(price, customer_type);

    calculator = AdjustmentsApplier(items, rush, customer_type, total)
    total = calculator.apply_adjustments(total)

    return round(total, 2)