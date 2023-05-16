from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("strombelete")
    ingredient2 = Ingredient("cream cheese")

    assert hash(ingredient1) == hash("strombelete")
    assert hash(ingredient1) != hash(ingredient2)

    assert ingredient1 == ingredient1
    assert ingredient1 != ingredient2

    assert repr(ingredient1) == "Ingredient('strombelete')"

    assert ingredient1.name == "strombelete"

    assert ingredient1.restrictions == set()
