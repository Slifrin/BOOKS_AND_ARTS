import json
import os

from typing import Dict, Any

def load() -> Dict:
    json_f_name = os.path.join(os.path.dirname(__file__), 'osconfeed.json')
    with open(json_f_name) as fp:
        return json.load(fp)


