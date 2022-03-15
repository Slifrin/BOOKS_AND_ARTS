"""Solution for 'logs' serialization"""

import json

from datetime import datetime
from ipaddress import IPv4Address

from log import logs, as_dict # uses asdict from dataclasses


def default(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    elif isinstance(obj, IPv4Address):
        return str(obj)
    return obj

for log in logs:
    data = json.dumps(as_dict(log), default=default)
    print(data)