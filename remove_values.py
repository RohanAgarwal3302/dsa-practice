# def removeElement(nums: list[int], val: int):
#         k=0
#         while val in nums:
#             nums.remove(val)          
#             k+=1
#         return nums

# print(removeElement([0,1,2,2,3,0,4,2],2))

d=[0,1,2,2,3,0,4,2]
d[:]=sorted(d)
print(d)