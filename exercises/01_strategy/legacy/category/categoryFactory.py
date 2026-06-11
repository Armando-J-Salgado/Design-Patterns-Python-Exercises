from category.category import Category
from category.bookCategory import BookCategory
from category.defaultCategory import DefaultCategory
from category.digitalCategory import DigitalCategory
from category.foodCategory import FoodCategory

class CategoryFactory:
    """
    Factory class
    """
    def generate_category(self, category):
        match category:
            case 'book':
                return BookCategory()
            case 'digital':
                return DigitalCategory()
            case 'food':
                return FoodCategory()
            case _:
                return DefaultCategory()
                