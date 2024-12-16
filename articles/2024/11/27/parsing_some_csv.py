import pathlib
from functools import wraps
import pandas as pd
import numpy as np
from joblib import Parallel, delayed
import time


def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        ret_val = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} {args} {kwargs} took {end - start:.4f}")
        return ret_val

    return wrapper


@time_it
def file_generator():
    for folder in ["CSV", "XLSX", "PICKEL"]:
        pathlib.Path(folder).mkdir(parents=True, exist_ok=True)

    for file_number in range(10):
        values = np.random.uniform(size=(20000, 25))
        pd.DataFrame(values).to_csv(f"CSV/{file_number}.csv")
        pd.DataFrame(values).to_excel(f"XLSX/{file_number}.xlsx")
        pd.DataFrame(values).to_pickle(f"PICKEL/{file_number}.pickel")


@time_it
def check_excel():
    frames = [pd.read_excel(f"XLSX/{file_numer}.xlsx") for file_numer in range(10)]

    final_frame = pd.concat(frames)
    print(f"Final frame length {len(final_frame)}")


@time_it
def check_csv():
    frames = [pd.read_csv(f"CSV/{file_numer}.csv") for file_numer in range(10)]

    final_frame = pd.concat(frames)
    print(f"Final frame length {len(final_frame)}")


# @time_it
# def universal_check(file_type: str):
#     frames = [pd.read_excel(f"{file_type.upper()}/{file_numer}.{file_type.lower()}") for file_numer in range(10)]

#     final_frame = pd.concat(frames)
#     print(f"{file_type} Final frame length {len(final_frame)}")


@time_it
def check_joblib():
    def worker(file_location):
        return pd.read_csv(file_location)

    frames = Parallel(n_jobs=-1, verbose=10)(
        delayed(worker)(f"CSV/{file_numer}.csv") for file_numer in range(10)
    )
    final_frame = pd.concat(frames, ignore_index=True)
    print(f"Final frame length {len(final_frame)}")

@time_it
def check_pickle_in_parallel():
    def worker(file_location):
        return pd.read_pickle(file_location)

    frames = Parallel(n_jobs=-1, verbose=10)(
        delayed(worker)(f"PICKEL/{file_numer}.pickel") for file_numer in range(10)
    )
    final_frame = pd.concat(frames, ignore_index=True)
    print(f"Final frame length {len(final_frame)}")

def main() -> None:
    print(f"Hello main from : {__file__}")
    # file_generator()

    # check_excel()
    check_csv()
    print("-" * 50) 
    check_joblib()
    print("-" * 50) 
    check_pickle_in_parallel()


if __name__ == "__main__":
    main()
