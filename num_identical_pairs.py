# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# nums = [1,2,3,1,1,3]
# ans: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

# completed

def numIdenticalPairs(nums:list[int]):
    j=0
    i=1
    k=0
    while j!=len(nums)-1:
        if nums[j]==nums[i]:
            k+=1
        i+=1
        if i==len(nums):
            j+=1
            i=j+1
    return k

print(numIdenticalPairs([1,1,1,1]))