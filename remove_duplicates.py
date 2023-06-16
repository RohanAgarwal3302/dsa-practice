def removeDuplicates(nums:list[int]):
    result=[nums[0]]
    k=0
    for i in range(1,len(nums)):
        if nums[i] not in result: 
            result.insert(i,nums[i])
            k+=1
    diff=len(nums)-len(result)
    for i in range(1,diff):
        result.append(0)     
    return result #new array is created


def removeDuplicates(nums:list[int]):
    k=0
    for i in range(0,len(nums)):
        while nums.count(nums[i])>1 and nums[i]>0:
            if nums[i]==nums[i+1]:
                nums.remove(nums[i+1])
                nums.append(0)
                k+=1
    k=len(nums)-k
    return k #time limit exceeded

def removeDuplicates(nums:list[int]):
    j=1
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]:            
            nums[j]=nums[i]
            j+=1
    return j

def removeDuplicates(nums:list[int]):
    nums[:]=set(nums)
    return len(nums)


print(removeDuplicates([1,1,1,1,3,4,4,4,5,5,5,5,6,6,6,6]))