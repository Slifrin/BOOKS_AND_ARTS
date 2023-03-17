import requests
import time



def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all(urls):
    with requests.Session() as session:
        for url in urls:
            download_site(url, session)


def main() -> None:
    print(f'Hello main from : {__file__}')
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration}s")


if __name__ == '__main__':
    main()