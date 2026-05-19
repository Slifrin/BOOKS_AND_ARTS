from __future__ import annotations

import logging
import sys

from functools import wraps

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

if TYPE_CHECKING:
    from collections.abc import Callable


# it is important that there are TWO !!!! [[]] around input in return type annotations
def log_exception[**P, R](logger: logging.Logger, prefix_msg: str) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator_func(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if prefix_msg:
                    logger.error("%s %s %s", prefix_msg, str(e), func.__name__)
                else:
                    logger.error("%s %s", str(e), func.__name__)
                raise
        return wrapper
    return decorator_func


def log_exception_simpler(logger: logging.Logger, prefix_msg: str):
    def decorator_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception:
                if prefix_msg:
                    logger.exception("%s %s", prefix_msg, func.__name__)
                else:
                    logger.exception("%s", func.__name__)
                raise
        return wrapper
    return decorator_func

class LazyKwargs:
    __slots__ = ("kwargs",)

    def __init__(self, kwargs: dict):
        self.kwargs = kwargs

    def __str__(self) -> str:
        return ", ".join("%s=%r" % (k, v) for k, v in self.kwargs.items())


def log_tool_call(tool_name: str, **params) -> None:
    msg = "Tool {0} called with: {1}"
    print(msg.format(tool_name, LazyKwargs(params)))
    logger.info("Tool %s called with: %s", tool_name, LazyKwargs(params))


@log_exception(logger=logger, prefix_msg="Handling tarapaty")
def tarapaty_f():
    sum = 0
    for i in range(4, -1, -1):
        print(1 / i)
        sum += i
    return sum


@log_exception_simpler(logger=logger, prefix_msg="Handling tarapaty")
def tarapaty_f2():
    sum = 0
    for i in range(4, -1, -1):
        print(1 / i)
        sum += i
    return sum

def main() -> None:
    print(f"Hello main from : {__file__} executed by {sys.executable}")

    log_tool_call("compile", target="x86", opt_level=2, debug=True)

    print(tarapaty_f2())


if __name__ == "__main__":
    main()
