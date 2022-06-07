def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    lowest_pair_dif = float("inf")
    lowest_pair = ()
    for num1 in nums:
        num2 = goal - num1
        if num2 in nums and nums.index(num2) >= nums.index(num1):
            if (nums.index(num2)-nums.index(num1)) < lowest_pair_dif:
                lowest_pair_dif = nums.index(num2)-nums.index(num1)
                lowest_pair = (num1, num2)
    return lowest_pair

