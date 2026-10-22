def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        l = r = k = 0
        while l < len(left) and r < len(right):
            if arr[l] < arr[r]:
                arr[k] = arr[l]
                k=k+1 
                l=l+1
            else:
                arr[k] = arr[r]
                k = k+1
                r = r+1
        
        while l < len(left):
            arr[k] = arr[l]
            k= k+1
            l = l+1

        while r < len(right):
                    arr[k] = arr[r]
                    k= k+1
                    r = r+1



arr = eval(input("Enter the elements: "))
print(f'Unsorted Array -> {arr}')
merge_sort(arr)
print(f'Sorted Array -> {arr}')