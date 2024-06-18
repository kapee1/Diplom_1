from praktikum.burger import Burger
from unittest.mock import Mock
import pytest


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        mock_buns = Mock()
        bun_name = 'Булочка'
        mock_buns.get_name.return_value = bun_name
        burger.set_buns(mock_buns)

        assert burger.bun.get_name() == bun_name

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient_first = Mock()
        mock_ingredient_second = Mock()
        burger.add_ingredient(mock_ingredient_first)
        burger.add_ingredient(mock_ingredient_second)
        burger.move_ingredient(0, 1)

        assert burger.ingredients == [mock_ingredient_second, mock_ingredient_first]

    def test_get_price(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 3 # цена за одну булочку, в бургере их две
        mock_ingredient.get_price.return_value = 2.5
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == (mock_bun.get_price() * 2 + mock_ingredient.get_price())

    def test_get_receipt(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = 'Начинка'
        mock_ingredient.get_name.return_value = 'Лист салата'
        mock_ingredient.get_price.return_value = 75.5
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Пшеничная булочка'
        mock_bun.get_price.return_value = 25.3
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        expected_result = ('(==== Пшеничная булочка ====)\n''= начинка Лист салата =\n'
                           '(==== Пшеничная булочка ====)\n''\n''Price: 126.1')
        assert burger.get_receipt() == expected_result

