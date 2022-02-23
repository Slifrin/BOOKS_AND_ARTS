"""
https://adamj.eu/tech/2021/05/10/python-type-hints-how-to-use-typeddict/
"""

from typing import TypedDict


class SalesSummary(TypedDict):
    sales: int
    country: str
    product_codes: list[str]

def get_sales_summary() -> SalesSummary:
    """Return summary for yesterday’s sales."""
    return {
        "sales": 1_000,
        "country": "UK",
        "product_codes": ["SUYDT"],
    }


def main():
    print('Hello main')
    sales_summary = get_sales_summary()
    sales = sales_summary["sales"]
    print("Sales per hour:", round(sales / 24, 2))
    

if __name__ == '__main__':
    main()