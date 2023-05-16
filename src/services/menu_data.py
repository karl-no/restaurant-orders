import pandas as pd
from models.dish import Dish, Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.df = pd.read_csv(source_path)

        dishes = {}

        for data in self.df.itertuples(index=False):
            dish, price, ingredient, recipe_amount = data
            if dish not in dishes:
                dish_info = Dish(dish, price)
                dishes[dish] = dish_info
                self.dishes.add(dish_info)

            ingredient_info = Ingredient(ingredient)
            dishes[dish].add_ingredient_dependency(
                ingredient_info,
                recipe_amount
            )
