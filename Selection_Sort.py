def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i          #assume i is  min itself
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:                         #to find min position index
                min = j  # update minimum index

        arr[i], arr[min] = arr[min], arr[i]  # SWAP


arr=eval(input("Enter the element: "))
print(f'Unsorted Array : {arr}')
selection_sort(arr)
print(f'Sorted Array: {arr}')
