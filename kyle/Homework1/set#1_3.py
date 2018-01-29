#!/usr/bin/python

ColumnNumber=2
ColumnData=[]
with open("sample.txt") as file_txt:
	for line in file_txt:
		ColumnData.append(line[ColumnNumber-1])
print ColumnData
