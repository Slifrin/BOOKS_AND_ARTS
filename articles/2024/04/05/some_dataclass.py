import dataclasses

from typing import Optional

@dataclasses.dataclass
class PageInfoToCrawl:

    url: str
    form_data: Optional[dict] = None
    number_of_executions: int = 0


def main() -> None:
    print(f'Hello main from : {__file__}')
    info = PageInfoToCrawl(url="https://fiz.org/buz")
    print(dataclasses.asdict(info))


if __name__ == '__main__':
    main()