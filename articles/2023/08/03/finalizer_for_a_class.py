import weakref
import shutil

class TempDir:
    def __init__(self, name) -> None:
        self.name = name
        self._finalizer = weakref.finalize(self, shutil.rmtree, self.name)

    def remove(self):
        self._finalizer()

    @property
    def removed(self):
        return not self._finalizer.alive

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exec_val, exc_tb):
        self.remove()



def main() -> None:
    print(f'Hello main from : {__file__}')
    tmp = TempDir("MY_tmp_dir")
    print("Bye bye")

if __name__ == '__main__':
    main()