import random
import time


def unique_sum_list(nums):
    total = 0
    seen = []
    for n in nums:
        if n in seen:
            continue
        total += n
        seen.append(n)
    return total

def unique_sum_set(nums):
    total = 0
    seen = set()
    for n in nums:
        if n in seen:
            continue
        total += n
        seen.add(n)
    return total

def unique_sum_dict(nums):
    total = 0
    seen = {}
    for n in nums:
        if n in seen:
            continue
        total += n
        seen[n] = None
    return total

def unique_sum_tuple(nums):
    total = 0
    seen = ()
    for n in nums:
        if n in seen:
            continue
        total += n
        seen = (*seen, n)
    return total




def main() -> None:
    print(f'Hello main from : {__file__}')
    n = 10000
    nums = [random.randint(0, 2 << 32) for _ in range(n)]
    for unique_sum in [
        unique_sum_tuple,
        unique_sum_list,
        unique_sum_set,
        unique_sum_dict
    ]:
        start = time.perf_counter()
        total = unique_sum(nums)
        elapsed = time.perf_counter() - start
        print(f"{unique_sum.__name__}: {elapsed * 1000:.3f}")


# big difference in 'add' operater and 'in' operator
# list and tuple looping over elements O(N)
# set and dict calculate hash and check where this val would go O(1)
# appending tuple is O(N) as there needs to be a copy
# list, set dict amortized addition as adding one O(N) is expensive adding many is similar O(N)
# as theresomtimes are recalculations

if __name__ == '__main__':
    main()
