from fake_enum_test import Dummy


def create_dummy_instance_and_call_f():

    # value = Dummy.FIRST.value
    # print(value)
    instnce = Dummy.FIRST.value()
    print(instnce.f())
    print("After calling f")