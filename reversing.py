def bubble_sort(nums:list[int]):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]>nums[j]:
                v=nums[j]
                nums[j]=nums[i]
                nums[i]=v
    return nums

print(bubble_sort([98,100,53,903,34,76,25]))


