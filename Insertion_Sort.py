def insertion_sort(arr):
    for i in range(1,len(arr)):
        j = i-1
        temp = arr[i]
        while temp < arr[j] and j>=0:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = temp

arr = eval(input("Enter your elements: "))
print("Unsorted array:", arr)
insertion_sort(arr)
print("Sorted array:", arr)
