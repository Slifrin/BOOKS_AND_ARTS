
# iterable and iterator are the same object

class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

def iterablle_and_iterator_same_object():
    y = yrange(3)
    print(next(y))
    print(next(y))
    print(next(y))
    # print(next(y)) # raise stop iteration
    y2 = yrange(3)
    l = list(y2)
    print(l)

# iterable and iterator are diffrent objects

class zrange:
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        return zrange_iter(self.n)

class zrange_iter:
    def __init__(self, n):
        self.i = 0
        self.n = n
    
    def __iter__(self):
        # Iterators are iterables too.
        # Adding this functions to make them so.
        return self
    
    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

def main():
    print(f'Hello main from : {__file__}')




if __name__ == '__main__':
    main()