import sys
import os

# not a good option
current_path = os.path.dirname(__file__)
sys.path.append(current_path + "/..")

"""
Note that when using from package import item, the item can be
either a submodule (or subpackage) of the package, or some other
name defined in the package, like a function, class or variable.
The import statement first tests whether the item is defined in
the package; if not, it assumes it is a module and attempts to
load it. If it fails to find it, an ImportError exception is raised.


Contrarily, when using syntax like import item.subitem.subsubitem,
each item except for the last must be a package; the last item can
be a module or a package but can’t be a class or function or
variable defined in the previous item.
"""
import pack1.sub2.mod2


def main() -> None:
    print(f'Hello main from : {__file__}')
    pack1.sub2.mod2.f()


if __name__ == '__main__':
    main()