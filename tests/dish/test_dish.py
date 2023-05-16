from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    ingredient1 = Ingredient("ovo")
    dish1 = Dish("bolo", 20.00)
    dish2 = Dish("rocambole", 10.00)

    dish1.add_ingredient_dependency(ingredient1, 1)

    assert dish1.name == "bolo"

    assert hash(dish1) == hash(dish1)
    assert hash(dish1) != hash(dish2)

    assert dish1.__eq__(dish1) is True
    assert dish1.__eq__(dish2) is False

    assert repr(dish1) == "Dish('bolo', R$20.00)"

    with pytest.raises(TypeError):
        Dish("bolo", "biscoito")

    with pytest.raises(ValueError):
        Dish("bolo", 0)

    assert dish1.get_ingredients() == {
        Ingredient("ovo")
    }

    assert dish1.get_restrictions() == {Restriction.ANIMAL_DERIVED}
