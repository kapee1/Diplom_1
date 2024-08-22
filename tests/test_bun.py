import pytest

from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize('name', ([''], ['123'], ['Пшеничная'], ['Очень длинное название']))
    def test_get_bun_name(self, name):
        bun = Bun(name, 23)

        assert bun.get_name() == name

    @pytest.mark.parametrize('price', ([0, 0], [1], [22, 34], [99999999999]))
    def test_get_price(self, price):
        bun = Bun('Булочка', price)

        assert bun.get_price() == price

