# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    mergeSort(left)
    mergeSort(right)

    merge_sorted_arrays(left,right,arr)


def merge_sorted_arrays(left,right,arr):
    i,j,k = 0,0,0
    l, r= len(left), len(right)
    while i<l and j<r:
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]= right[j]
            j+=1
        k+=1
    while i<l:
        arr[k]=left[i]
        k+=1
        i+=1
    while j<r:
        arr[k]= right[j]
        j+=1
        k+=1

# write your code here

# Code to print the list
def printList(arr):
    l,i = len(arr),0
    while i<l:
        print(arr[i],end=' ')
        i+=1


# write your code here

# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("\nSorted array is: ", end="\n")
    printList(arr)