import contextlib
import io


def main() -> None:
    print(f'Hello main from : {__file__}')
    with contextlib.redirect_stdout(io.StringIO) as f:
        help(pow)
    s = f.getvalue()


if __name__ == '__main__':
    main()