import contextlib
import time

def acquire_resource(*args, **kwargs):
    print(args)
    print(kwargs)
    return "Some resource"


def release_resource(resource):
    print(f"Releasing {resource}")


# While many objects natively support use in with statements,
# sometimes a resource needs to be managed that isn’t a context
# manager in its own right, and doesn’t implement a close()
# method for use with contextlib.closing

@contextlib.contextmanager
def managed_resource(*args, **kwargs):
    resource = acquire_resource(*args, **kwargs)
    try:
        yield resource
    finally:
        release_resource(resource)


@contextlib.asynccontextmanager
async def get_connection():
    conn = await acquire_db_connection()
    try:
        yield conn
    finally:
        await release_db_connection(conn)



# Context managers defined with asynccontextmanager()
# can be used either as decorators or with async with statements:

@contextlib.asynccontextmanager
async def timeit():
    now = time.monotonic()
    try:
        yield
    finally:
        print(f"it took {time.monotonic() - now}s to run")


# When used as a decorator, a new generator instance is implicitly
# created on each function call. This allows the otherwise “one-shot”
# context managers created by asynccontextmanager() to meet the
# requirement that context managers support multiple invocations
# in order to be used as decorators.

@timeit()
async def a_main():
    async with get_connection() as conn:
        return conn.query("SELECT ...")



def main() -> None:
    print(f'Hello main from : {__file__}')

    with managed_resource(timeout=3600) as resource:
        print(resource)


if __name__ == '__main__':
    main()