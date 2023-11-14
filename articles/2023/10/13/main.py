import os
import sys
from functools import wraps
from time import perf_counter


from PIL import Image

import pytesseract
import tesserocr

def search_for_tesseract_ocr():
    # for root, dirs, files in os.walk("/usr/share/tesseract-ocr/"):
    #     print(f"{root=}")
    #     print(f"{dirs=}")
    #     print(f"{files=}")
    print(os.environ)
    for element in os.listdir("/usr/share/tesseract-ocr/"):
        print(element)

search_for_tesseract_ocr()

def check_time(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        f(*args, **kwargs)
        finish = perf_counter()
        print(f"It took {finish - start}")
    return wrapper

@check_time
def check_pytesseract():
    print(f"Check {check_pytesseract.__name__}")
    print(pytesseract)
    print(pytesseract.image_to_string(Image.open("./some_word.png")))


@check_time
def check_tesserocr():
    print(f"Check {check_tesserocr.__name__}")
    print(tesserocr.tesseract_version())  # print tesseract-ocr version
    print(tesserocr.get_languages())  # prints tessdata path and list of available languages
    image = Image.open("./some_word.png")
    print(tesserocr.image_to_text(image))  # print ocr text from image
    # or
    print(tesserocr.file_to_text("./some_word.png"))

def main() -> None:
    print(f'Hello main from : {__file__}')
    print(sys.version)
    print(sys.version_info)

    check_pytesseract()
    check_tesserocr()



if __name__ == '__main__':
    main()