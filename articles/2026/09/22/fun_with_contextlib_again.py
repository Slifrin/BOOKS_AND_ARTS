import contextlib
import io
import os
import sys

from urllib.request import urlopen


class SimpleContext:
    def __enter__(self):
        print("starting context")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("Closing context")
        print(id(self))
        print(exc_type)
        print(exc)
        print(tb)
        return False


def simple_case():
    with SimpleContext() as tmp:
        print("Inside custom dummy context", id(tmp))


def acquire_resource(*args, **kwargs):
    print(f"Calling with {args=} {kwargs=}")
    return 123


def release_resource(resource):
    print(f"release {id(resource)}")


def simple_case_with_contextlib():
    @contextlib.contextmanager
    def manged_resource(*args, **kwargs):
        resource = acquire_resource(*args, **kwargs)
        try:
            yield resource
        finally:
            release_resource(resource)

    with manged_resource(timeout=180) as resource:
        print(resource)


def example_of_closing():
    with contextlib.closing(urlopen("https://www.python.org")) as page:
        print(len(page.read()))

def example_of_suppress():
    with contextlib.suppress(FileNotFoundError):
        os.remove("Some_bla_bla_file.exe")


def example_of_output_redirect():
    with contextlib.redirect_stdout(io.StringIO()) as f:
        help(pow)
    s = f.getvalue()
    print(f"{len(s)=} {s[:30]}...")

def example_of_context_decorator():
    """
This change is just syntactic sugar for any construct of the following form:

def f():
    with cm():
        # Do stuff

    """
    class myctx(contextlib.ContextDecorator):
        def __enter__(self):
            print("starting")
        def __exit__(self, *exc):
            print("Finishing")
            return False

    @myctx()
    def function():
        print("the bit in the middle")

    function()

def check_exit_stack():
    def exit_callback(*args, **kwargs):
        print(args)
        print(kwargs)

    file_names = [f"tmp_{i}.txt" for i in range(1, 5)]
    with contextlib.ExitStack() as stack:
        stack.callback(exit_callback)
        files = [stack.enter_context(open(fname, "w")) for fname in file_names]
        for f in files:
            print(f)

    with contextlib.ExitStack() as stack:
        stack.callback(exit_callback)
        files = [stack.enter_context(open(fname, "w")) for fname in file_names]
        close_files = stack.pop_all().close
        print(close_files)

def main() -> None:
    print(f"Hello main from : {__file__} executed by {sys.executable}")
    simple_case()
    simple_case_with_contextlib()
    example_of_closing()
    example_of_suppress()
    example_of_output_redirect()
    example_of_context_decorator()
    check_exit_stack()

if __name__ == "__main__":
    main()
