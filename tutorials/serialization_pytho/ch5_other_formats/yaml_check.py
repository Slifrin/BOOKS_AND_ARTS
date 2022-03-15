
from pprint import pprint

import yaml


with open('config.yaml', 'r') as fp:
    config = yaml.safe_load(fp)

    pprint(config)

    print(yaml.safe_dump(config))