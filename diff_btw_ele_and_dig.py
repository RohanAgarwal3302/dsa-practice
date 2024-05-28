# You are given a positive integer array nums.

# The element sum is the sum of all the elements in nums.
# The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
# Return the absolute difference between the element sum and digit sum of nums.

# Note that the absolute difference between two integers x and y is defined as |x - y|.

# nums = [1,15,6,3]
# The element sum of nums is 1 + 15 + 6 + 3 = 25.
# The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.
# The absolute difference between the element sum and digit sum is |25 - 16| = 9.

# completed

def differenceOfSum(nums: list[int]):
    e=0
    d=0
    for v in nums:
        e+=v
        while v!=0:
            d+=v%10
            v//=10
    return abs(e-d)

def differenceOfSum(nums: list[int]):
    e=sum(nums)
    d=0
    for v in nums:
        while v!=0:
            d+=v%10
            v//=10
    return abs(e-d)


print(differenceOfSum([1,15,6,3]))    