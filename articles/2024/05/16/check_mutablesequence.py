from collections.abc import MutableSequence


class SimpleMapping(MutableSequence):
    def __init__(self):
        self.internal_list = []

    def __len__(self):
        return len(self.internal_list)

    def __getitem__(self, i):
        return self.internal_list[i]

    def __delitem__(self, i):
        del self.internal_list[i]

    def __setitem__(self, i, new_item):
        self.internal_list[i] = new_item

    def __str__(self):
        return str(self.internal_list)

    def insert(self, index, new_item):
        self.internal_list.insert(index, new_item)


def check_some_gen():
    simple_test = SimpleMapping()
    simple_test.append(1)
    simple_test.append(2)
    simple_test.append(3)

    yield from simple_test

def main() -> None:
    print(f'Hello main from : {__file__}')
    
    for x in check_some_gen():
        print(x)
    
if __name__ == '__main__':
    main()