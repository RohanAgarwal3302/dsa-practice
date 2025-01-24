# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# nums1 = [1,2,2,1], nums2 = [2,2]
# ans: [2,2]

# completed

def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    def element_count(list):
        dict={}
        i,j=0,len(list)-1
        while i<=j:
            if i==j:
                if list[i] in dict.keys():
                    dict[list[i]]+=1
                else:
                    dict[list[i]]=1
                return dict
            if list[i] in dict.keys():
                dict[list[i]]+=1
            else:
                dict[list[i]]=1
            if list[j] in dict.keys():
                dict[list[j]]+=1
            else:
                dict[list[j]]=1
            i+=1
            j-=1
        return dict
    
    dict1=element_count(nums1)
    dict2=element_count(nums2)
    result=[]
    keys=dict1.keys()
    
    for key in dict2.keys():
        if key in dict1.keys():
            result+=[key]*min(dict1[key],dict2[key])
    return result

print(intersect([1,2,2,1],[2,2]))