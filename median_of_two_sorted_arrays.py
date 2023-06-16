def findMedianSortedArrays(nums1: list[int], nums2: list[int]):
        nums=sorted(nums1+nums2)
        if len(nums)%2==1:
            return nums[len(nums)//2]
        else: 
            return (nums[len(nums)//2-1]+nums[(len(nums)//2)])/2

print(findMedianSortedArrays([1,2],[3,4,8,10,11]))