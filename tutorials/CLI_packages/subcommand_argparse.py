import argparse
import sys


def creat(args):
    print(f'Creating project "{args.name}" with {args.files} files')

def delete(args):
    print(f'Deleting project "{args.name}" {"with all files" if args.all else ""}')


def main() -> None:
    # print(f'Hello main from : {__file__} executed by {sys.executable}')
    parser = argparse.ArgumentParser(description='Project managment tool')
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # command configuration
    create_parser = subparsers.add_parser('create', help='Create new project')
    create_parser.add_argument('name', help='Project name')
    create_parser.add_argument('--files', type=int, default=3, help='Number of files')
    create_parser.set_defaults(func=creat)

    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a project')
    delete_parser.add_argument('name', help='Project name')
    delete_parser.add_argument('--all', action='store_true', help='Delete all files')
    delete_parser.set_defaults(func=delete)

    args = parser.parse_args()
    print('hello args', args)
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()