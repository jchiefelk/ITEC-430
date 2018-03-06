#!/usr/bin/python

def bubbleSort(numlist):
	n = len(numlist)

	for i in range(n):
		for j in range (0, n-i-1):
			if numlist[j] > numlist[j+1]:
				numlist[j], numlist[j+1] = numlist[j+1], numlist[j]

numlist = [100, 5, 9, 20, 1000, 3, 17, 87, 74]
bubbleSort(numlist)
print("Sorted array is:")
print(numlist)

