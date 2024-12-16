import functools


@functools.total_ordering
class Studnet:
    def __init__(self, fisrstname: str, lastname: str):
        self.firstname = fisrstname
        self.lastname = lastname

    def _is_valid_oerand(self, other):
        return hasattr(other, "firstname") and hasattr(other, "lastname")

    def __eq__(self, other):
        if not self._is_valid_oerand(other):
            return NotImplemented
        return (self.firstname.lower(), self.lastname.lower()) == (
            other.firstname.lower(),
            other.lastname.lower(),
        )

    def __lt__(self, other):
        if not self._is_valid_oerand(other):
            return NotImplemented
        return (self.firstname.lower(), self.lastname.lower()) < (
            other.firstname.lower(),
            other.lastname.lower(),
        )


def main() -> None:
    print(f"Hello main from : {__file__}")


if __name__ == "__main__":
    main()
