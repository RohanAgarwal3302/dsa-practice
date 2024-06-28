# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

# Return the answer in an array.

# nums = [8,1,2,2,3]
# ans: [4,0,1,1,3]
# Explanation: 
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1). 
# For nums[3]=2 there exist one smaller number than it (1). 
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

# completed

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