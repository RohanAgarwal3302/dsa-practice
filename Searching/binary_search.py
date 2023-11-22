def binary_search(arr: list[int],target: int):
    l=0
    r=len(arr)    
    while l!=r:
        mid=(l+r)//2
        if target==arr[mid]:
            return mid
        elif target<mid:
            r=mid-1
        else:
            l=mid+1
    return -1

print(binary_search([17, 18, 19, 30, 34, 47, 67],67))