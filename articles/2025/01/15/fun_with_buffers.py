import io
import itertools


def my_batch(iterable, n=2):
    iterator = iter(iterable)
    while batch := tuple(itertools.islice(iterator, n)):
        yield batch


def main() -> None:
    print(f"Hello main from : {__file__}")
    t = io.BytesIO()
    t.write(b"abcdefghijklmnoprstuw")
    t.seek(0)
    with open("tmp.b", "wb") as o_b:
        for batch in my_batch(t.read(), 5):
            print([chr(e) for e in batch])
            print(batch)

        print(len(t.getbuffer()))
        n = 0
        increment = 5
        while n < len(t.getbuffer()):
            print(t.getbuffer()[n : n + increment].tobytes())
            val = o_b.write(t.getbuffer()[n : n + increment])
            print(val)
            n += increment
    
    with open("tmp.b", "rb") as i_b:
        print(i_b.read())

if __name__ == "__main__":
    main()
