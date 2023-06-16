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