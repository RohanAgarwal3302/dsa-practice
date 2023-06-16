def runningSum(nums: list[int]):
        v=0
        ans=[]
        for i in range(len(nums)):
            v+=nums[i]
            ans.append(v)
        return ans