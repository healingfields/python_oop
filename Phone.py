from Item import Item


class Phone(Item):
    pay_rate = 0.7

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)

        # validations
        assert broken_phones >= 0, f"broken phones {broken_phones} is not positive or equal to zero"

        # assignements
        self.broken_phones = broken_phones
