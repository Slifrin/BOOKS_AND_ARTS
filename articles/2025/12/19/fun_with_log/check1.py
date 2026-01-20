"""
Docstring for articles.2025.12.19.fun_with_log.check1
https://betterstack.com/community/guides/logging/how-to-start-logging-with-python/
docs.python.org/3/howto/logging.html
"""


import sys


import logging

logging.basicConfig(level=logging.INFO)




def main() -> None:
    print(f'Hello main from : {__file__} executed by {sys.executable}')


if __name__ == '__main__':
    main()