from praktikum.ingredient import Ingredient
import praktikum.ingredient_types


class TestIngredient:

    TYPE_SAUCE = praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE
    TYPE_FILLING = praktikum.ingredient_types.INGREDIENT_TYPE_FILLING
    NAME = 'neutral'
    PRICE = 420

    def test_get_price(self):
        ingredient = Ingredient(self.TYPE_SAUCE, self.NAME, self.PRICE)

        assert ingredient.get_price() == self.PRICE

    def test_get_name(self):
        ingredient = Ingredient(self.TYPE_SAUCE, self.NAME, self.PRICE)

        assert ingredient.get_name() == self.NAME

    def test_get_type(self):
        ingredient = Ingredient(self.TYPE_FILLING, self.NAME, self.PRICE)

        assert ingredient.get_type() == self.TYPE_FILLING
