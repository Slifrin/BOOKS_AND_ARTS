import array
import datetime

from io import BytesIO

import msgpack


def packing_multiple_values():
    buf = BytesIO()
    for i in range(100):
        buf.write(msgpack.packb(i))

    buf.seek(0)
    unpacker = msgpack.Unpacker(buf)

    for unpacked in unpacker:
        print(unpacked)


def packing_custom_data():
    useful_dict = {
        "id": 1,
        "created": datetime.datetime.now(),
    }

    def encode_datetime(obj):
        if isinstance(obj, datetime.datetime):
            return {"__datetime__": True, "as_str": obj.strftime("%Y%m%dT%H:%M:%S.%f")}
        return obj

    def decode_datetime(obj):
        if "__datetime__" in obj:
            obj = datetime.datetime.strptime(obj["as_str"], "%Y%m%dT%H:%M:%S.%f")
        return obj

    packed_dict = msgpack.packb(useful_dict, default=encode_datetime)

    this_dict_again = msgpack.unpackb(packed_dict, object_hook=decode_datetime)

    print(this_dict_again)


def using_extended_types():
    def default(obj):
        if isinstance(obj, array.array) and obj.typecode == 'd':
            return msgpack.ExtType(42, obj.tobytes())
        raise TypeError("Unknown type: %r" % (obj,))

    def ext_hook(code, data):
        if code == 42:
            a = array.array('d')
            a.frombytes(data)
            return a
        return msgpack.ExtType(code, data)

    data = array.array('d', [1.2, 3.4])
    packed = msgpack.packb(data, default=default)
    print(packed)
    unpacked = msgpack.unpackb(packed, ext_hook=ext_hook)
    print(unpacked)



def main() -> None:
    print(f"Hello main from : {__file__}")
    packed_value = msgpack.packb([1, 2, 3])
    print(packed_value)
    unpacked_value = msgpack.unpackb(packed_value)
    print(unpacked_value)

    packing_multiple_values()

    packing_custom_data()

    using_extended_types()


if __name__ == "__main__":
    main()
