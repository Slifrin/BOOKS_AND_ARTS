import bz2
import csv
from typing import NamedTuple, Callable
from datetime import datetime

class Column(NamedTuple):
    src: str
    dest: str
    convert: Callable

def parse_timestamp(text):
    return datetime.strptime(text, "%Y-%m-%d %H:%M:%S")

columns = [
    Column("VendorID", "vendor_id", int),
    Column("VendorID", "vendor_id", int),
]