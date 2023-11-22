def bubble_sort(arr: list[int]):
    swapped=False
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            return arr
    return arr

print(bubble_sort([67,34,18,19,30,17,47]))