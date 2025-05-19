import json
import sys

from collections import defaultdict


class NestedDict(defaultdict):
    def __init__(self, value=None):
        super().__init__(NestedDict)
        self.value = value


def main() -> None:
    print(f"Hello main from : {__file__} executed by {sys.executable}")

    nested_dict = lambda: defaultdict(nested_dict)
    nest = nested_dict()

    nest[0][1] = 6

    tmp = NestedDict()
    tmp[1][2][3][4] = "check"

    print(json.dumps(tmp))
    print(tmp.items())
    print(tmp.values())

    tmp2 = defaultdict()
    tmp2[1] = defaultdict()
    tmp2[1][2] = defaultdict()
    tmp2[1][2] = "check_2"

    print(json.dumps(tmp2))
    print(tmp2.items())
    print(tmp2.values())


if __name__ == "__main__":
    main()
