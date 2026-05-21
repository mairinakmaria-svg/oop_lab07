from rational import Rational, RationalValueError


class RationalList:
    def __init__(self, values=None):
        self.items = []
        if values is not None:
            for value in values:
                self.append(value)

    def append(self, value):
        if not isinstance(value, Rational):
            raise RationalValueError(value, "adding to RationalList")
        self.items.append(value)

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __str__(self):
        return "[" + ", ".join(str(item) for item in self.items) + "]"

    def sum(self):
        result = Rational(0)
        for item in self.items:
            result = result + item
        return result
