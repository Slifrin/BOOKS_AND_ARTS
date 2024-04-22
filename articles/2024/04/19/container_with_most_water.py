


def maxArea_simple(height: list[int]) -> int:
    max_area = 0
    for i, h1 in enumerate(height):
        for j, h2 in enumerate(height[i+1:]):
            area = min(h1, h2) * (j + 1)
            print(area, h1, h2, j, i)
            if area > max_area:
                max_area = area
    return max_area


def maxArea(height: list[int]) -> int:
    """
    https://www.geeksforgeeks.org/container-with-most-water/
s
    Solution Analysis – Why this solution works?
    Everytime, we are moving our pointer i ahead if height of line at ith index is smaller or j
    pointer if height of line at jth index is smaller. This means whichever line is smaller,
    we won’t consider it again, because, this line could be the answer only if the other line is larger
    than it and at maximum width and to be noticed that this is the time when other line is larger as well
    as max distance apart. So, not considering it makes sense.
    In other words, we are required to pair up every line with that line which is greater than it and at maximum distance apart i.e. 
    For example -> 8 5 9 1 10 2 6
    here, if 8 has to be in the answer then other line that we choose should be 10 as it is the
    first line from the end that is at maximum distance apart from 8 and longer than 8. Hence, for 8 to be in the answer, other line should be 10.
    Now, Lets assume i at 8 and j at 10. Compare it and move the pointer i to 5.
    Now, you may ask, ok, you have moved the pointer i to 5 but can it not happen that 5 could pair up
    with other lines after 10 as we have neglected those lines by moving j pointer to 10.
    So, to be noticed that if 5 would have been in the answer then any line after 10 must be >= 5 and if there is
    any line after 10 whose height is greater than or equal to 5 then its contribution would surely have been calculated while pointer ‘i’ was at 8.
    So, for the combinations of lines which we are neglecting, have been already taken care of.
    """

    max_area = 0
    i = 0
    j = len(height) - 1
    max_area = 0
    while i != j:
        h1 = height[i]
        h2 = height[j]
        area = min(h1, h2) * (j - i)
        if area > max_area:
            max_area = area
        if h1 > h2:
            j -= 1
        else:
            i += 1
    return max_area


def maxArea_little_faster(height: list[int]) -> int:
    max_area = 0
    i = 0
    j = len(height) - 1
    max_area = 0
    while i != j:
        if height[i] > height[j]:
            area = height[j] * (j - i)
            j -= 1
        else:
            area = height[i] * (j - i)
            i += 1
        if area > max_area:
                max_area = area
    return max_area


def main() -> None:
    print(f'Hello main from : {__file__}')
    # print(maxArea_simple([1,8,6,2,5,4,8,3,7]))
    print(maxArea([1,8,6,2,5,4,8,3,7]))
    print(maxArea([8,5,9,1,10,2,6]))


if __name__ == '__main__':
    main()