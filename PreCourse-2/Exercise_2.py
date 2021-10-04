# Python program for implementation of Quicksort Sort

# give you explanation for the approach
def partition(arr, low, high):
    pivot_ind=low
    pivot = arr[pivot_ind]
    l= len(arr)
    while low<high:
        while low<l and arr[low]<=pivot:
            low+=1
        while arr[high]>=pivot:
            high-=1
        if low<high:
            arr[low],arr[high] =arr[high],arr[low]
    if arr[high]!=pivot:
        arr[high], arr[pivot_ind]= arr[pivot_ind],arr[high]
    return high



# Function to do Quick sort
def quickSort(arr, low, high):
    if low<high:
        partition_ind=partition(arr, low, high)
        quickSort(arr,low,partition_ind-1)
        quickSort(arr,partition_ind+1,high)

# write your code here

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),