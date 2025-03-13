import argparse

from pprint import pprint
,

class VerboseStore(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print(f'Storing {values} in the {option_string} option...')
        setattr(namespace, self.dest, values)


parser = argparse.ArgumentParser(
    prog="Fun_with_args",
    description="Command description",
    epilog="bottom description",
    # argument_default=argparse.SUPPRESS
)
group1 = parser.add_argument_group("group1")
group1.add_argument("--foo", help="foo of the %(prog)s program")
group2 = parser.add_argument_group("group2")
group2.add_argument("--list", help="List all avilable sources")

parser.add_argument('--bar', action='store_const', const=42)
parser.add_argument('--list_sources', action='store_true')
parser.add_argument("source_name", nargs='?')

parser.add_argument('-n', '--name', action=VerboseStore)
# parser.print_help()
args = parser.parse_args()

pprint(args)
