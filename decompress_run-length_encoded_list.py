# arr=[0]*4
# # arr.append(0)*4

# print(arr)

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
        return arr

print(decompressRLElist([1,2,3,4]))