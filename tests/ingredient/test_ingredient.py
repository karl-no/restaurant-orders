from src.models.ingredient import (Ingredient, Restriction)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("ovo")
    ingredient2 = Ingredient("farinha")

    assert hash(ingredient1) == hash("ovo")
    assert hash(ingredient1) != hash(ingredient2)

    assert ingredient1 == ingredient1
    assert ingredient1 != ingredient2

    assert repr(ingredient1) == "Ingredient('ovo')"

    assert ingredient1.name == "ovo"

    assert ingredient1.restrictions == {Restriction.ANIMAL_DERIVED}
