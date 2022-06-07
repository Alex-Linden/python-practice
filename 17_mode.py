import math

def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    most_common = -math.inf  # float('-inf') works too
    for val in nums:
        if nums.count(val) > most_common:
            most_common = val

    return most_common
