import sys
import pandas as pd


def get_dummy_frame():
    return pd.DataFrame(
        {
            "a": [1, 3],
            "b": [2, 4],
        },
    )


def main() -> None:
    print(f"Hello main from : {__file__} executed by {sys.executable}")
    print(get_dummy_frame())


if __name__ == "__main__":
    main()
