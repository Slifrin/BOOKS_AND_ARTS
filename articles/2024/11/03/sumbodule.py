from enum import Enum, EnumMeta


class MyEnumMeta(EnumMeta):
    def __str__(cls):
        lines = [f"Members of '{cls.__name__}' are:"]
        for member in cls:
            lines.append(f"- {member}")
        return "\n".join(lines)

    def _contains(self, member):
        return member in self._member_map_ or member in set(
            map(lambda x: x.value, self._member_map_.values())
        )

    def is_valid(self, member):
        return self._contains(member)


class Color(Enum, metaclass=MyEnumMeta):
    RED = 1
    GREEN = 2
    BLUE = 3


def foo(color_type):
    if Color.is_valid(color_type):
        print(f"Wonderful! we will use the wonderful {color_type} color")
        return "valid"
    else:
        print(f"{color_type} is not supported color. The supported colors are:\n{str(color_type)}")
        return "invalid"



def examples_of_color_usage():
    print(Color)

    foo("RED")
    foo("YELLOW")
