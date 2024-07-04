# Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

# answer.length == nums.length.
# answer[i] = |leftSum[i] - rightSum[i]|.
# Where:

# leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
# rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
# Return the array answer.

# nums = [10,4,8,3]
# ans: [15,1,11,22]
# Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
# The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

# completed

def leftRigthDifference(nums:list[int]):
        r=0
        l=0
        ans=[]
        for v in nums:
            r+=v
        r=r-nums[0]
        ans.append(r)
        for i in range(1,len(nums)):
            r=r-nums[i]
            l+=nums[i-1]
            ans.append(abs(l-r))
        return ans
    
def leftRigthDifference(nums:list[int]):
    lsum=0
    rsum=sum(nums)
    ans=[]
    for i in range(len(nums)):
        if i>0:
            lsum+=nums[i-1]
        rsum-=nums[i]
        ans.append(abs(lsum-rsum))
    return ans

print(leftRigthDifference([10,4,8,3]))