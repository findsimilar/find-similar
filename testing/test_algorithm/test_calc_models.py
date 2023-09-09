"""
Test calc_models
"""
from find_similar.calc_models import Item


class TestItem:
    """
    Test Item class
    """
    def test_eq(self):
        """
        Test eq magic method
        """
        one = Item(
            id=1,
            label="one",
            part_number="some part",
            id_shop=1,
            id_base_item=0,
            cos=0,
        )

        two = Item(
            id=2,
            label="two",
            part_number="some part",
            id_shop=1,
            id_base_item=1,
            cos=0,
        )

        assert one == two
