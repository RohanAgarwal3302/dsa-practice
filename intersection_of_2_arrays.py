# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order.

# nums1 = [1,2,2,1], nums2 = [2,2]
# ans: [2]

# completed

def intersection(nums1: list[int], nums2: list[int]):
        set1=set(nums1)
        set2=set(nums2)
        result=[]
        if len(set2)<len(set1):
            for c in set1:
                if c in set2:
                    result.append(c)
        else:
            for c in set2:
                if c in set1:
                    result.append(c)
        return result

print(intersection([1,2,2,1],[2,2]))