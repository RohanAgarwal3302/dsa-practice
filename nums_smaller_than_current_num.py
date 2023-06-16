def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
    ans=[]
    i=0
    while i!=len(nums):           
        c=0
        for j in range(len(nums)):
            if i!=j:
                if nums[j]<nums[i]:
                    c+=1
        ans.append(c)
        i+=1
    return ans

def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
    s_nums=sorted(nums)
    dic={}
    dic[s_nums[0]]=0
    for i in range(1,len(nums)):
        if s_nums[i]!=s_nums[i-1]:
            dic[s_nums[i]]=i
    for i in range(len(nums)):
        nums[i]=dic[nums[i]]
    return nums


print(smallerNumbersThanCurrent([8,1,2,2,3]))
        