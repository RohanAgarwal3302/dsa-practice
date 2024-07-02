# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.

# Return the array ans.

# nums = [1,2,1]
# ans: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]

# complete

def getConcatenation(nums: list[int]):
        i=0
        ans=[]
        while i<=len(nums)-1:
            ans.insert(i,nums[i])
            ans.insert(i+len(nums),nums[i])
            i+=1
        return ans

def getConcatenation(nums: list[int]):
        ans=[]
        for i in range(0,len(nums)):
            ans.insert(i,nums[i])
            ans.insert(i+len(nums),nums[i])
        return ans

def getConcatenation(nums: list[int]):
      return nums+nums

def getConcatenation(nums: list[int]):
      nums.extend(nums)
      return nums
  
print(getConcatenation([1,2,1]))