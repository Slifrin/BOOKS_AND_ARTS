"""
It would be easier to just copy paste
https://github.com/mCodingLLC/VideosSampleCode/blob/master/videos/104_multiprocessing_pool/multiprocessing_pool.py
"""

import pathlib
import numpy as np
from scipy.io.wavfile import write


def generate_audio(output_dir: pathlib.Path):
    print(output_dir)
    output_dir.parent.mkdir(parents=True, exist_ok=True)
    seconds = 360
    sample_rate = 44100
    fs = 100
    t = np.linspace(0., 1. * seconds, sample_rate * seconds)
    # print(len(t))
    aplitude = np.iinfo(np.int64).max
    data = aplitude * np.sin(2. * np.pi * fs * t)
    write(output_dir, sample_rate, data.astype(np.int64))


def main() -> None:
    print(f'Hello main from : {__file__}')
    my_path = pathlib.Path(__file__)
    print(f'{my_path.parent}')
    filenames = [my_path.parent / 'sounds' / f'example{n}.wav' for n in range(24)]
    for filename in filenames:
        generate_audio(filename)

if __name__ == '__main__':
    main()