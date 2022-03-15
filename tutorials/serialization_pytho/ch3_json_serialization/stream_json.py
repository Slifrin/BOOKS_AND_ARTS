"""
    Streaming json data
    One object per line
"""

import json
from io import BytesIO

groups = [
    {'animal' : 'bee', 'group' : 'swarm'},
    {'animal' : 'fox', 'group' : 'charm'},
    {'animal' : 'whale', 'group' : 'pod'},
]


# Sending side
network = BytesIO()
for message in groups:
    data = json.dumps(message)
    network.write(data.encode('utf-8')) # Socket work in byte level
    network.write(b'\n')

# Receiving side
network.seek(0) # Go bask to start of data for reading it

while True:
    line = network.readline()
    if not line:
        break
    received_data = json.loads(line)
    print("GOT ", received_data)