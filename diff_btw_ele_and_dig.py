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