from enum import Enum

class Command(Enum):
    QUIT = 0
    RESET = 1


def structural_pttern_maaching(input_data: str):
    match input_data:
        case "quit":
            print("By then")
        case "reset":
            print("here we go again")
        case _:
            print("Default ... I don't know what to do")


def pattern_with_enum(input_enum: Command):
    match input_enum:
        case Command.QUIT:
            print("By then")
        case Command.RESET:
            print("Here we go again")


def pattern_with_multiple_elements(command: str):
    match command.split(): # it is possible to pass multiple emenets
        case ["quit"]: # only one element
            print("By then")
        case ["load", filename]: # two elements from split one is exact string and other is any other str
            print(f"Loading data from {filename}")
        case ["save", filename]: # similar case
            print(f"Saving data in {filename}")
        case _: # wildcard match
            print(f"Uknown command {command}")


def possible_pattern_matching(data):
    match data:
        case "a": ...
        case ["a", "b"]: ...
        case ["a", value1]: ...
        case ["a", *values]: ...
        case ("a"|"b"|"c"): ...
        case ("a"|"b"|"c") as pattern: ...
        case ["a", value2] if value2 in ["b", "c", "d"]: ...
        case ["z", _]: ... # any collection of items

def patterns_with_objects(media_type):
    match media_object:
        case Image(type="jpg"):
            # Return as-is
            return media_object
        case Image(type="png") | Image(type="gif"):
            return render_as(media_object, "jpg")
        case Video():
            raise ValueError("Can't extract frames from video yet")
        case other_type:
            raise Exception(f"Media type {media_object} can't be handled yet")

def pattersn_with_object_argument(media_object):
    match media_object:
        case Image(type=media_type):
            print (f"Image of type {media_type}")


def main() -> None:
    print(f'Hello main from : {__file__}')


if __name__ == '__main__':
    main()