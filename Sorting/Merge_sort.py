def merge_sort(nums:list[int]):
    l=len(nums)//2
    for i in range(0,l):
        # if nums[i]<nums[-(i+1)]:
        v=nums[-(i+1)]
        nums[-(i+1)]=nums[i]
        nums[i]=v
    return nums

print(merge_sort([1,4,3,65,23,78,13,89,45,27]))

