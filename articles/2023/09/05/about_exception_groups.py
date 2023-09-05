"""
    https://realpython.com/python311-exception-groups/
"""
import logging

logger = logging.getLogger("exception_group")
logger.setLevel(logging.DEBUG)


def basic_info():
    err_g1 = ExceptionGroup("one error", [ValueError(654)])
    print(err_g1)
    err_g2 = ExceptionGroup("two errors", [ValueError(321), TypeError("int")])
    print(err_g2)

    err_g_nested = ExceptionGroup(
        "nested",
        [
            ExceptionGroup(
                "imports",
                [ImportError("no_such_module"), ModuleNotFoundError("another_module")],
            ),
            TypeError("int"),
        ],
    )
    print(err_g_nested)

    try:
        raise err_g_nested
    except ExceptionGroup as e_g:
        # logger.info(e_g, exc_info=True)
        logger.exception(e_g)


def some_handling():
    def possible_but_incorrectt():
        try:
            raise ExceptionGroup("group", [ValueError(564)])
        except ExceptionGroup as eg:
            for err in eg.exceptions:
                if isinstance(err, ValueError):
                    print("Handling ValueError")
                if isinstance(err, TypeError):
                    print("Handling TypeError")

    possible_but_incorrectt()

    def better_way():
        """
        Several except* clauses may trigger.
        except* clauses that match an error remove that error from the exception group.
        """
        try:
            raise ExceptionGroup("group", [ValueError(564)])
        except* ValueError:
            print("Handling ValueError in a better way")
        except* TypeError:
            print("Handling TypeError in a better way")

    better_way()

    def more_complex():
        try:
            raise ExceptionGroup(
                "group", [TypeError("str"), ValueError(564), TypeError("int")]
            )
        except* ValueError as eg:
            print(f"Handling ValueError in a better way {eg.exceptions}")
        except* TypeError as eg:
            print(f"Handling TypeError in a better way {eg.exceptions}")

    more_complex()

    def partial_handling():
        try:
            raise ExceptionGroup(
                "group", [TypeError("str"), ValueError(564), TypeError("int")]
            )
        except* ValueError as eg:
            print(f"Handling ValueError in a better way {eg.exceptions}")

    try:
        partial_handling()
    except ExceptionGroup as err_g:
        logger.exception(err_g)

def more_on_regualr_exceptions():
    try: 
        raise ValueError(446)
    except* ValueError as eg:
        print(type(eg), eg.exceptions)




def main() -> None:
    print(f"Hello main from : {__file__}")
    print(f"{issubclass(ExceptionGroup, Exception)=}")

    basic_info()
    some_handling()
    more_on_regualr_exceptions()


if __name__ == "__main__":
    main()
