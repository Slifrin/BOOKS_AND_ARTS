import os
from collections import Counter
import urllib.request
import xml.etree.ElementTree as ET

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, 'feed')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().lower()


def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    tree_root = ET.fromstring(content) # this parse to the root 
    tags = Counter()

    for e in tree_root[0]:
        if e.tag.lower() == "item":
            for category in e.findall("category"):
                tags[category.text] += 1
    return tags.most_common(n)



def main() -> None:
    print(f'Hello main from : {__file__}')
    print(get_pybites_top_tags())

if __name__ == '__main__':
    main()