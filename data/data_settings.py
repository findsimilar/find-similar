"""
Settings to work with data
"""
SHEET_NUMBER = 0
START_ROW = 0
TRUE_CODE_LENGTH = 11


class ContractorInfo:
    """
    Model for contractor
    """
    def __init__(
        self, part_column_num: int, label_column_num: int, shop_name: str, **kwargs
    ):
        self.part_column_num = part_column_num
        self.label_column_num = label_column_num
        self.shop_name = shop_name

        for key, val in kwargs.items():
            setattr(self, key, val)

    def __eq__(self, other):
        return self.shop_name == other.shop_name


BASE_VENDOR = ContractorInfo(2, 1, "AVZ")
