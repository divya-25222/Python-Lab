
def quick_sort(arr, start, end):
    if start >= end:
        return

    pivot = arr[(start + end) // 2]
    i = start
    j = end

    while i <= j:
        while arr[i] < pivot:
            i = i + 1

        while arr[j] > pivot:
            j = j - 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]  # SWAP
            i = i + 1
            j = j - 1

    if start < j:
        quick_sort(arr, start, j)

    if i < end:
        quick_sort(arr, i, end)


arr = eval(input("Enter the elements: "))
print("Unsorted array:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
