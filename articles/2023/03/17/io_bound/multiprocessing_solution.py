import requests
import multiprocessing
import time


session = None


def set_global_session():
    global session
    if not session:
        session = requests.Session()


def download_one(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name}:READ {len(response.content)} from {url} with {id(session)}")


def download_all(urls):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_one, urls)


def main() -> None:
    print(f'Hello main from : {__file__}')
    urls = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all(urls)
    duration = time.time() - start_time
    print(f"Downloaded {len(urls)} in {duration}s")

if __name__ == '__main__':
    main()