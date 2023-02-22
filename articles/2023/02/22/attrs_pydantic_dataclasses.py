"""
    https://www.youtube.com/watch?v=zN4VCb0LbQI
"""
from with_datclasses import check_dataclass_part
from with_attrs import check_attrs_part
from with_pydantic import check_pydantic_part

def main() -> None:
    print(f'Hello main from : {__file__}')
    # check_dataclass_part()
    # check_attrs_part()
    check_pydantic_part()


if __name__ == '__main__':
    main()