def linear_search(arr: list[int],target: int):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

print(linear_search([67,34,18,19,30,17,47],30))