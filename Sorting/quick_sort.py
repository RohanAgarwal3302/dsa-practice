def partition(arr: list[int], low: int, high: int):
    pivot= arr[low]
    i=low + 1
    j=high
    while True:
        while i<=j and arr[i]<=pivot:
            i+=1
        while i<=j and arr[j]>=pivot:
            j-=1
        if i<=j:
            arr[i],arr[j]=arr[i],arr[j]
        else: 
            break
    pivot,arr[j]=arr[j],pivot
    return j

def quick_sort(arr: list[int], low: int, high: int):
    if low<high:
        pivot=partition(arr,low,high)
        quick_sort(arr,low,pivot-1)
        quick_sort(arr,pivot+1,high)
    return arr

print(quick_sort([67,34,18,19,30,17,47],0,len([67,34,18,19,30,17,47])-1))