import pathlib


def check_current_path():
    current = pathlib.Path(__file__)
    print(current)
    print(current.parent)
    new_dir = current.parent / 'pdf_samples'
    print(new_dir)

def main() -> None:
    print(f'Hello main from : {__file__}')
    check_current_path()

if __name__ == '__main__':
    main()