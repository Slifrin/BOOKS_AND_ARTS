

class Root:
    def draw(self):
        assert not hasattr(super(), 'draw')

class Shape(Root):
    def __init__(self, shapename, **kwargs):
        self.shapename = shapename
        super().__init__(**kwargs)
    def draw(self):
        print(f"Drawing... Setting shape to: {self.shapename}")
        super().draw()

class ColoredShape(Shape):
    def __init__(self, color, **kwargs):
        self.color = color
        super().__init__(**kwargs)
    def draw(self):
        print(f"Drawing... Setting color to {self.color}")
        return super().draw()

class Movable:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        print(f"Drawing at position {self.x} : {self.y}")

class MovableAdapter(Root):
    def __init__(self, x, y, **kwargs):
        self.movable = Movable(x, y)
        super().__init__(**kwargs)
    def draw(self):
        self.movable.draw()
        super().draw()

class MovableColoredShape(ColoredShape, MovableAdapter):
    pass


def main() -> None:
    print(f'Hello main from : {__file__}')
    cs = ColoredShape(color='red', shapename='circle')
    cs.draw()
    print("*" * 80)
    MovableColoredShape(color='green', shapename='triangle', x=10, y=20).draw()

if __name__ == '__main__':
    main()