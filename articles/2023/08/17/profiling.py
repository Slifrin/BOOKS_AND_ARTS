import re
import time

import requests


def count_https_in_web_pages():
    with open("top15USWebsites.txt", "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f.readlines()]
    
    print(urls)

    htmls = []
    for url in urls:
        htmls = htmls + [requests.get(url).text]

    print(f"Number of sites {len(htmls)}")
    count_https = 0
    count_http = 0
    for html in htmls:
        count_https += len(re.findall("https://", html))
        count_http += len(re.findall("http://", html))
    
    print("finished parsing")
    time.sleep(2)

    print(f"{count_https=}")
    print(f"{count_http=}")
    print(f"{count_https/count_http=}")



def main() -> None:
    print(f'Hello main from : {__file__}')

    import cProfile
    import pstats

    start = time.perf_counter()

    with cProfile.Profile() as pr:
        count_https_in_web_pages()
    
    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)

    print(f"Total time: {time.perf_counter() - start}")

    stats.print_stats(30)

if __name__ == '__main__':
    main()