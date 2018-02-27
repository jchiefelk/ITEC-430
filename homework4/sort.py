# Python program for implementation of Bubble Sort
 
def bubbleSort(numlist):
    n = len(numlist)
 
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if numlist[j] > numlist[j+1]:
            	numlist[j], numlist[j+1] = numlist[j+1], numlist[j] #array swap
 

# unsorted list
numlist = [64, 34, 25, 12, 22, 11, 90] 
bubbleSort(numlist)
print("Sorted array is:")
print(numlist)