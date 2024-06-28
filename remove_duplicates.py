# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
# The remaining elements of nums are not important as well as the size of nums.
# Return k.

# nums = [1,1,2]
# ans: 2, nums = [1,2,_]
# Explanation: Function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# completed

def removeDuplicates(nums:list[int]):
    result=[nums[0]]
    k=0
    for i in range(1,len(nums)):
        if nums[i] not in result: 
            result.insert(i,nums[i])
            k+=1
    diff=len(nums)-len(result)
    for i in range(1,diff):
        result.append(0)     
    return result #new array is created


def removeDuplicates(nums:list[int]):
    k=0
    for i in range(0,len(nums)):
        while nums.count(nums[i])>1 and nums[i]>0:
            if nums[i]==nums[i+1]:
                nums.remove(nums[i+1])
                nums.append(0)
                k+=1
    k=len(nums)-k
    return k #time limit exceeded

def removeDuplicates(nums:list[int]):
    j=1
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]:            
            nums[j]=nums[i]
            j+=1
    return j

def removeDuplicates(nums:list[int]):
    return len(set(nums))

# def removeDuplicates(nums:list[int]): working on a new method
#     i=0
#     j=1
#     while j<len(nums):
#         if nums[i]!=nums[j]:
#             i+=1
#         j+=1

print(removeDuplicates([1,1,1,1,3,4,4,4,5,5,5,5,6,6,6,6]))