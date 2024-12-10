# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

# nums = [4,5,6,7,0,1,2], target = 0
# ans: 4

# completed

def search(nums: list[int], target: int):
        if target in nums:
            return nums.index(target)
        else:
            return -1 ## O(n)

def search(nums: list[int], target: int):
    start,end=0,len(nums)
    if target in nums:
        while start!=end:
            mid=(start+end)//2        
            if nums[mid]==target:
                return mid
            elif nums[mid]>=nums[start]:
                if target>=nums[start] and target<nums[mid]:
                    end=mid
                else:
                    start=mid+1
            else:
                if target<=nums[end-1] and target>nums[mid]:
                    start=mid+1
                else:
                    end=mid
        return mid
    else: 
        return -1 ## O(log n)
    
print(search([4,5,6,7,0,1,2],0))