# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

# nums = [1,2,3,4]
# ans: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

# completed

def runningSum(nums: list[int]):
        v=0
        ans=[]
        for i in range(len(nums)):
            v+=nums[i]
            ans.append(v)
        return ans
    
def runningSum(nums: list[int]):
    for i in range(1,len(nums)):
        nums[i]=nums[i]+nums[i-1]
    return nums

print(runningSum([1,2,3,4]))