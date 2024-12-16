import json

from pprint import pprint


class ExtendedEncoder(json.JSONEncoder):
    def default(self, obj):
        name = type(obj).__name__
        try:
            encoder = getattr(self, f'encode_{name}')
        except AttributeError:
            super().default(obj)
        else:
            encoded = encoder(obj)
            encoded['__extended_json_type__'] = name
            return encoded

class ExtendedDecoder(json.JSONDecoder):
    def __init__(self, **kwargs):
        kwargs['object_hook'] = self.object_hook
        super().__init__(**kwargs)


    def object_hook(self, obj):
        try:
            name = obj['__extended_json_type__']
            decoder = getattr(self, f'decode_{name}')
        except (KeyError, AttributeError):
            return obj
        else:
            return decoder(obj)


class MyEncoder(ExtendedEncoder):
    def encode_complex(self, c):
        return {'real': c.real, 'imag': c.imag}

    def encode_range(self, r:range):
        return {"start": r.start, "stop": r.stop, "step": r.step}

class MyDecoder(ExtendedDecoder):
    def decode_complex(self, obj):
        return complex(obj["real"], obj["imag"])

    def decode_range(self, obj):
        return range(obj["start"], obj["stop"], obj["step"])


def main() -> None:
    print(f'Hello main from : {__file__}')
    value = {
        "hey": complex(1, 2),
        "there": range(1, 10, 3),
        73: False,
    }

    data = json.dumps(value, cls=MyEncoder)
    pprint(data)

    decoded_data = json.loads(data, cls=MyDecoder)
    print(decoded_data)
    

if __name__ == '__main__':
    main()