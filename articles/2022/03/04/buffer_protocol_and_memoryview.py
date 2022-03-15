"""
https://eli.thegreenplace.net/2011/11/28/less-copies-in-python-with-the-buffer-protocol-and-memoryviews/
"""

import os

def mor_efficient_way_to_read_into_bytearrat():
    f_name = 'test_bin_data'
    with open(f_name, 'rb') as i_f:
        data = bytearray(os.path.getsize(f_name))
        i_f.readinto(data)

        print(data)

"""
mybuf = ... # some large buffer of bytes
mv_mybuf = memoryview(mybuf) # a memoryview of mybuf
func(mv_mybuf[:len(mv_mybuf)//2])
  # passes the first half of mybuf into func as a "sub-view" created
  # by slicing a memoryview.
  # NO COPY is made here!

"""

def main():
    print('Hello main', __file__)
    mor_efficient_way_to_read_into_bytearrat()


if __name__ == '__main__':
    main()