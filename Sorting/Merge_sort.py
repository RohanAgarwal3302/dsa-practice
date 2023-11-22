def merge(left: list[int],right: list[int]):
    new=[]
    j,i=0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            new.append(left[i])
            i+=1
        else:
            new.append(right[j])
            j+=1
    new.extend(left[i:])
    new.extend(right[j:])
    return new

def merge_sort(arr: list[int]):
    if len(arr)<2:
        return arr
    mid=len(arr)//2
    r_arr=arr[:mid]
    l_arr=arr[mid:]
    r_arr=merge_sort(r_arr)
    l_arr=merge_sort(l_arr)
    return merge(l_arr,r_arr)

print(merge_sort([67,34,18,19,30,17,47]))