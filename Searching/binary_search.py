def binary_search(arr: list[int],target: int): ## for ascending
    l=0
    r=len(arr)
    while l!=r:
        if arr[l]==target:
            return l
        if r<len(nums):
            if arr[r]==target:
                return r
        if r<len(arr):
            if arr[r]==target:
                return r
        mid=(l+r)//2
        if target==arr[mid]:
            return mid
        elif target<arr[mid]:
            r=mid-1
        else:
            l=mid+1
    return -1

nums = [17, 18, 19, 30, 34, 47, 67]

print(binary_search(nums,34))

def binary_search(arr: list[int],target: int): ## for descending
    l=0
    r=len(arr) 
    while l!=r:
        if arr[l]==target:
            return l
        if r<len(nums):
            if arr[r]==target:
                return r
        mid=(l+r)//2
        if target==arr[mid]:
            return mid
        elif target>arr[mid]:
            r=mid-1
        else:
            l=mid+1
    return -1

nums = [17, 18, 19, 30, 34, 47, 67]

# print(binary_search(nums,34))

nums = nums[::-1]

print(binary_search(nums,19))