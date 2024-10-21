
from io import BytesIO, StringIO

import pandas as pd


def check_pandas():
    test_data = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(test_data)
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, sep='|', index=False)

    print('hello')

    """
    tmp.getvalue()
    b'|col1|col2\n0|1|3\n1|2|4\n'
    csv_buffer.getvalue()
    '|col1|col2\n0|1|3\n1|2|4\n'
    csv_buffer
    <_io.StringIO object at 0x116c06440>
    csv_buffer.seek(0)
    0
    pd.read_csv(csv_buffer, sep='|')
    Unnamed: 0  col1  col2
    0           0     1     3
    1           1     2     4
        
    """


def add_data_to_dataframe():
    test_data = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(test_data)

    print(df)
    df.loc[len(df)] = [5,6]
    print(df)


def main() -> None:
    print(f'Hello main from : {__file__}')
    # check_pandas()
    add_data_to_dataframe()


if __name__ == '__main__':
    main()