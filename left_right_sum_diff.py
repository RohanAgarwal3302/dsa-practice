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

print(leftRigthDifference([10,4,8,3]))