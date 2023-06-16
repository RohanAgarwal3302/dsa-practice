def searchRange(nums: list[int], target: int):
        start,end=0,len(nums)
        if target in nums:
            while start!=end:
                first=(start+end)//2
                if nums[first]==target:
                    break
                elif nums[first]<=target:
                    start=first+1
                else: end=first
            nums[:]=reversed(nums)
            start=0
            end=len(nums)
            while start!=end:
                second=(start+end)//2
                if nums[second]==target:
                    break
                elif nums[second]<=target:
                    start=second+1
                else: end=second
            return first,second
        else:
            return -1,-1
        
print(searchRange([5,7,7,8,8,10],8))
        