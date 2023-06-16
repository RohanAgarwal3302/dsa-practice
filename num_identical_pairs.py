def numIdenticalPairs(nums:list[int]):
    j=0
    i=1
    k=0
    while j!=len(nums)-1:
        if nums[j]==nums[i]:
            k+=1
        i+=1
        if i==len(nums):
            j+=1
            i=j+1
    return k


print(numIdenticalPairs([1,1,1,1]))