from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Pool
import time
import scipy.io.wavfile
import numpy as np

def etl(filename: str) -> tuple[str, float]:
    # extract
    start_t = time.perf_counter()
    samplerate, data = scipy.io.wavfile.read(filename)

    # do some transformation
    eps = .1
    data = data + np.random.normal(scale=eps, size=len(data))
    data = np.clip(data, -1.0, 1.0)

    # load (store new form)
    new_filename = filename.removesuffix(".wav") + "-transformed.wav"
    scipy.io.wavfile.write(new_filename, samplerate, data)
    end_t = time.perf_counter()
    
    return filename, end_t - start_t


def etl_demo():
    filenames = [f"sounds/example{n}.wav" for n in range(24)]
    start = time.perf_counter()
    
    print("starting etl")
    for filename in filenames:
        _, duration = etl(filename)
        print(f"{filename} completed in {duration:.2f}")

    end_t = time.perf_counter()
    total_duration = end_t - start
    print(f"etl took {total_duration:.2f}s total")

def etl_demo_multiproccess():
    filenames = [f"sounds/example{n}.wav" for n in range(24)]
    start = time.perf_counter()
    
    print("starting etl")
    with Pool() as pool:
        # results = pool.map(etl, filenames)
        # results = pool.imap(etl, filenames)
        results = pool.imap_unordered(etl, filenames)
        for filename, duration in results:
            print(f"{filename} completed in {duration:.2f}")

    end_t = time.perf_counter()
    total_duration = end_t - start
    print(f"etl took {total_duration:.2f}s total")




def main() -> None:
    print(f'Hello main from : {__file__}')
    etl_demo_multiproccess()

if __name__ == '__main__':
    main()