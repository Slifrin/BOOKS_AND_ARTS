
class DummyClass:
    def __init__(self, *args, **kwargs):
        print(f"{self=} {args=} {kwargs=}")

    def f(self, *args, **kwargs):
        print(f"{self=} {args=} {kwargs=}")