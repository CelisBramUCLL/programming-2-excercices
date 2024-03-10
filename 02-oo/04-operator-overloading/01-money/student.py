class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.__currency = currency

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value

    @property
    def currency(self):
        return self.__currency

    def __add__(self, other):
        if self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        else:
            raise RuntimeError("Mismatched currecies!")

    def __sub__(self, other):
        if self.currency == other.currency:
            return Money(self.amount - other.amount, self.currency)
        else:
            raise RuntimeError("Mismatched currecies!")

    def __mul__(self, value):
        if value >= 0:
            return Money(self.amount * value, self.currency)
        else:
            raise ValueError("Value cannot be negative")
