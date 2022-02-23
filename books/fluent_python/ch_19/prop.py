

def quantity(storage_name):

    def qty_getter(instance):
        return instance.__dict__[storage_name]

    def qty_setter(instance, value):
        if value > 0:
            instance.__dict__[storage_name] = value
        else:
            raise ValueError('value must be > 0')

    return property(qty_getter, qty_setter)



class LineItem:
    weight = quantity('__weight')
    price = quantity('__price')

    def __init__(self, description, weight, price) -> None:
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


def main():
    item = LineItem('potatos', 5, 11)

    print(item.weight)
    print(item.price)
    print(item.subtotal())


if __name__ == '__main__':
    main()