import contextlib
import os


def main() -> None:
    print(f'Hello main from : {__file__}')
    with contextlib.suppress(FileNotFoundError):
        os.remove("somefile.tmp")
    
    with contextlib.suppress(FileNotFoundError):
        os.remove("somefile.tmp")
    

if __name__ == '__main__':
    main()