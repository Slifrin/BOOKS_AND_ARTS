import json

from datetime import datetime

import msgpack

type_key = '__type__'
datetime_type = 'datetime'


def default(obj):
    if isinstance(obj, datetime):
        return {
            type_key : datetime_type,
            'value' : obj.isoformat()
        }
    return obj

def object_hook(obj):
    if obj.get(type_key) == datetime_type:
        return datetime.fromisoformat(obj['value'])
    return obj

metric = {
    'time' : datetime.now(),
    'name' : 'memory',
    'value' : 14.3,
    'labels' : {
        'host' : 'prod7',
        'version' : '1.2.3',
    },
}

data = msgpack.dumps(metric, default=default)
print('data size : ', len(data))

metric2 = msgpack.loads(data, object_hook=object_hook)
print('metric == metric2 ??? ', metric == metric2)


jdata = json.dumps(metric, default=default)
print("Size comparision ", len(data)/len(jdata))