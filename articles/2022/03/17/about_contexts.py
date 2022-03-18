"""
    https://docs.python.org/3/library/contextlib.html
"""

import contextlib


def variable_number_of_context_managers():
    with contextlib.ExitStack() as stack:
        for resourc in resources:
            stack.enter_context(resourc)
        if need_special_resource():
            special = acquire_special_resource()
            stack.callback(release_special_resouce, special)

def catching_exception_from_enter_method():
    stack = contextlib.ExitStack()
    try:
        x = stack.enter_context(cm)
    except Exception:
        # handle __enter__ xception
    else:
        with stack:
            # Handle normal case



def main():
    print(f'Hello main from : {__file__}')


if __name__ == '__main__':
    main()