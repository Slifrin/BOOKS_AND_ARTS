
import os



def get_path(filename):
    head, tail = os.path.split(filename)
    import pdb; pdb.set_trace()
    return head

filename = __file__
print(f'path: {get_path(filename)}')