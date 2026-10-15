def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]    #SWAP

arr=eval(input("Enter the element: "))
print(f'Unsorted Array : {arr}')
bubble_sort(arr)
print(f'Sorted Array: {arr}')
