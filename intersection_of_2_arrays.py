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