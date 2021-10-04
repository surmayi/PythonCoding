# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    pivot_ind = l
    pivot=arr[pivot_ind]
    while l<h:
        while l<len(arr) and arr[l]<=pivot:
            l+=1
        while arr[h]>=pivot:
            h-=1
        if l<h:
            arr[l],arr[h]= arr[h],arr[l]
    if pivot!=arr[h]:
        arr[pivot_ind],arr[h] =arr[h],arr[pivot_ind]
    return h


def quickSortIterative(arr, l, h):
    if l<h:
        partition_ind = partition(arr,l,h)
        quickSortIterative(arr,l,partition_ind-1)
        quickSortIterative(arr,partition_ind+1,h)



# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),