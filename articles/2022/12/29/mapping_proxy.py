"""
    https://adamj.eu/tech/2022/01/05/how-to-make-immutable-dict-in-python/

    There are several third party packages that provide immutable
    data structures, such as immutables and pyrsistent. 
"""

from types import MappingProxyType

def check1():
    power_levels = MappingProxyType(
        {
            "Bob": 9001,
            "Jon": 8000,
        }
    )
    print(power_levels["Bob"])
    print(power_levels["Jon"])

    print(list(power_levels.keys()))

    try:
        power_levels["Bob"] = 9002
    except TypeError:
        print("Don't change MappingProxyType")

def check2():
    original = {"Bob": 9001}
    proxy = MappingProxyType(original)

    print(proxy["Bob"])
    original["Bob"] = 100000
    print(proxy["Bob"])

def check_dict_mege_operator():
    power_levels = MappingProxyType(
        {
            "Bob": 9001,
            "Jon": 8000,
        }
    )
    tom_beter = MappingProxyType(power_levels | {"Tom": 7000})
    print(tom_beter)

def main() -> None:
    print(f'Hello main from : {__file__}')
    check1()
    check2()
    check_dict_mege_operator()

if __name__ == '__main__':
    main()