"""Basic usage of JSON"""

import json

from datetime import datetime

from event import event

def default(obj):
    """Encode datetime to string in YYYY-MM-DDTHH:MM:SS format (RFC3339)"""
    if isinstance(obj, datetime):
        return obj.isoformat()
    return obj


def pairs_hook(pairs):
    """Convert the "time" key to datetime"""
    obj = {}
    for key, value in pairs:
        if key == 'time':
            value = datetime.fromisoformat(value)
        obj[key] = value
    return obj


def main():
    print('Hello main')
    data = json.dumps(event, default=default) # serialization custom types
    print(data)

    deserialized_data = json.loads(data, object_pairs_hook=pairs_hook) # deserialization of data
    print(deserialized_data)

if __name__ == '__main__':
    main()