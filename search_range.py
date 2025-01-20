# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# nums = [5,7,7,8,8,10], target = 8
# ans: [3,4]

# incomplete

def searchRange(nums: list[int], target: int):
        start,end=0,len(nums)
        if target in nums:
            while start!=end:  
                if nums[start]==target:
                    first=start
                    break
                if end<len(nums):
                    if nums[end]==target:
                        first=end
                        break
                first=(start+end)//2
                if nums[first]==target:
                    break
                elif nums[first]>target:
                    end=first-1
                else: 
                    start=first+1
            for second in range(first,len(nums)):
                if nums[second]!=target:
                    break
            else:
                return first,second
            return first,second-1
        return -1,-1
        
print(searchRange([5,7,7,8,8,10],8))
print(searchRange([3,3,3],3))
print(searchRange([1,2,3,3,3,3,4,5,9],3))
print(searchRange([],42))
print(searchRange([7,8,8,8,8,8,8,8,8,8,8,9],7))
print(searchRange([7,8,8,8,8,8,8,8,8,8,8,9],8))
print(searchRange([7,8,8,8,8,8,8,8,8,8,8,9],10))
print(searchRange([1,2,2,2,2,3,4,5,5,5,5,6,7,8,9,10,11,12,12,12,12,12,13],2))
print(searchRange([-999985131,-999953607,-999953607,-999915742,-999883817,-999849817,
-999822901,-999815377,-999810801,-68594,-49967,20394,114012,999969829,999973689,999975494],
-999953607))