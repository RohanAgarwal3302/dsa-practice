def selection_sort(nums:list[int]):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]>nums[j]:
                v=nums[j]
                nums[j]=nums[i]
                nums[i]=v
    return nums


def selection_sort(arr: list[int]):
    for i in range(len(arr)-1):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                min=j
                arr[i],arr[min]=arr[min],arr[i]
    return arr

print(selection_sort([67,34,18,19,30,173,472]))