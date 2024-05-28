# We are given a list nums of integers representing a list compressed with run-length encoding.

# Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).
# For each such pair, there are freq elements with value val concatenated in a sublist.
# Concatenate all the sublists from left to right to generate the decompressed list.

# Return the decompressed list.

# nums = [1,2,3,4]
# The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
# The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
# At the end the concatenation [2] + [4,4,4] is [2,4,4,4]. 

# completed
 
def decompressRLElist(nums: list[int]) -> list[int]:
        arr=[]
        for i in range(0,len(nums),2):
            arr+=[nums[i+1]]*nums[i]
        return arr

def decompressRLElist(nums: list[int]):
        arr=[]
        i=0
        while i<len(nums):
            arr+=[nums[i+1]]*nums[i]
            i+=2
        return arr

def decompressRLElist(nums: list[int]):
        arr=[]
        i=0
        while i<len(nums):
            arr2=[nums[i+1]]*nums[i]
            arr.extend(arr2)
            i+=2
        return arr ##least average time 

def decompressRLElist(nums: list[int]):
    if  len(nums)<3:
        return [nums[1]]*nums[0]
    else:
        return [nums[1]]*nums[0] + decompressRLElist(nums[2:]) # using recursion

print(decompressRLElist([1,2,3,4]))