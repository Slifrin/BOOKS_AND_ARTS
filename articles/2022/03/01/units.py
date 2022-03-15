import math


def set_unit(unit):

    def decorator_set_unit(func):

        func.unit = unit
        return func
    return decorator_set_unit

@set_unit("cm^3")
def volume(radius, height):
    return math.pi * radius**2 * height

print(volume(3, 5)) 
print(volume.unit)

def strange_unit(radius, height) -> "cm^3":
    return math.pi * radius**2 * height

