"""
    https://realpython.com/python-data-structures/
"""

import array

from collections import defaultdict, OrderedDict, namedtuple
from types import MappingProxyType, SimpleNamespace
from dataclasses import dataclass
from typing import NamedTuple
from struct import Struct

@dataclass
class Car:
    color: str
    mileage: float
    automatic: bool

class CarV2(NamedTuple):
    color: str
    mileage: float
    automatic: bool


def check_proxy_to_dixt():
    writable = {"one": 1, "two": 2}
    read_only = MappingProxyType(writable)
    print(read_only["one"])

    try:
        read_only["two"] = 3
    except TypeError as err:
        print(str(err))


def array_check():
    arr = array.array("f", (1.0, 2.0, 3.0, 3.5))
    print(arr[3])
    print(arr)


def bytearr_check():
    arr = bytearray((0, 1, 2, 3))
    print(arr[1])
    print(arr)
    try:
        arr[0] = 400
    except ValueError as err:
        print(str(err))


def datacls_check():
    car1 = Car("red", 23123.12, True)
    print(car1)


def namedtuples_check():
    car1 = CarV2("blue", 23123.12, False)
    print(car1)


def pack_data_into_struct():
    MyStruct = Struct("i?f")
    data = MyStruct.pack(23, False, 42.0)
    print(data)
    print(MyStruct.unpack(data))


def namespace_check():
    car1 = SimpleNamespace(color="red", mileage=3812.4, automatic=True)
    print(car1)
    car1.mileage = 12
    car1.windshield = "broken"
    print(car1)
    del car1.automatic
    print(car1)


def main():
    print(f'Hello main from : {__file__}')
    check_proxy_to_dixt()
    array_check()
    bytearr_check()
    datacls_check()
    namedtuples_check()
    pack_data_into_struct()
    namespace_check()


if __name__ == '__main__':
    main()