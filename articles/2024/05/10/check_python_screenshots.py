"""
    https://github.com/BoboTiG/python-mss
    https://stackoverflow.com/questions/35097837/capture-video-data-from-screen-in-python
"""

import numpy as np
import cv2
from mss import mss
from PIL import Image


def simple_example():
    with mss() as sct:
        sct.shot()


def more_complex_example():
    mon = {"left": 160, "top": 160, "width": 200, "height": 200}
    with mss() as sct:
        while True:
            screen_shot = sct.grab(mon)
            img = Image.frombytes(
                "RGB",
                (screen_shot.width, screen_shot.height),
                screen_shot.rgb,
            )
            cv2.imshow("test", np.array(img))
            # info about this if https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1
            if cv2.waitKey(33) & 0xFF in (
                ord("q"),
                27,
            ):
                break

    cv2.destroyAllWindows()


def better_example():
    bounding_box = {'top': 100, 'left': 0, 'width': 400, 'height': 300}
    
    with mss() as sct:
        while True:
            sct_grab = sct.grab(bounding_box)
            cv2.imshow('test_screen', np.array(sct_grab))

            if cv2.waitKey(0) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break


def main() -> None:
    print(f"Hello main from : {__file__}")
    # simple_example()
    more_complex_example()


if __name__ == "__main__":
    main()
