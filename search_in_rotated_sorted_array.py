# def search(nums: list[int], target: int):
#         if target in nums:
#             return nums.index(target)
#         else:
#             return -1

def search(nums: list[int], target: int):
    start,end=0,len(nums)
    if target in nums:
        while start!=end:
            mid=(start+end)//2        
            if nums[mid]==target:
                return mid
            elif nums[mid]>=nums[start]:
                if target>=nums[start] and target<nums[mid]:
                    end=mid
                else:
                    start=mid+1
            else:
                if target<=nums[end-1] and target>nums[mid]:
                    start=mid+1
                else:
                    end=mid
        return mid
    else: 
        return -1
    
print(search([4,5,6,7,0,1,2],0))
             

        

