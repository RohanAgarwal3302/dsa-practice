def buildArray(nums: list[int]):
        i=0
        ans=[]
        while i<=len(nums)-1:
            ans.insert(i,nums[nums[i]])
            i+=1
        return ans

print(buildArray([1,2,5,3,0,4]))