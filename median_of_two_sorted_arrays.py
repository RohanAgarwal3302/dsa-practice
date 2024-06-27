# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# nums1 = [1,3], nums2 = [2]
# ans: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# completed

def findMedianSortedArrays(nums1: list[int], nums2: list[int]):
    nums=sorted(nums1+nums2)
    if len(nums)%2==1:
        return nums[len(nums)//2]
    else: 
        return (nums[len(nums)//2-1]+nums[(len(nums)//2)])/2

def findMedianSortedArrays(nums1: list[int], nums2: list[int]):
    merged=[]
    i=0
    j=0
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<nums2[j]:
            merged.append(nums1[i])
            i+=1
        else:
            merged.append(nums2[j])
            j+=1
    merged.extend(nums1[i:])
    merged.extend(nums2[j:])
    if len(merged)%2==1:
        return merged[len(merged)//2]
    else: 
        return (merged[len(merged)//2-1]+merged[(len(merged)//2)])/2
        
print(findMedianSortedArrays([1,2],[3,4,8,10,11]))