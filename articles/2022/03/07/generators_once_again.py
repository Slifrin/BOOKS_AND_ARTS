"""
    https://realpython.com/introduction-to-python-generators/
"""

def is_palindrom(num):
    # skip single-digit inputs
    if num // 10 < 10:
        return False
    tmp = num
    reversed_num = 0

    while tmp != 0:
        reversed_num = (reversed_num * 10) + (tmp % 10)
        tmp = tmp // 10

    if num == reversed_num:
        return num
    else:
        return False


import cProfile

print(cProfile.run('sum([i * 2 for i in range(10000)])'))
print(cProfile.run('sum((i * 2 for i in range(10000)))'))


