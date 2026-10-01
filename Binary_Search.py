def binary_search(arr, search):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if search == arr[mid]:
            return True, mid
        elif search > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return False, -1

l1 = [10, 20, 30, 40, 50, 60]
found, pos = binary_search(l1, 30)
if found:
    print(f'Element found at position {pos}')
else:
    print("Element not found")