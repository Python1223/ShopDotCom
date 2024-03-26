class InvalidItemStringException(Exception):

    def __init__(self) -> None:
        super().__init__("Item String is invalid. Valid Items are : Blazer, Shirt etc")
