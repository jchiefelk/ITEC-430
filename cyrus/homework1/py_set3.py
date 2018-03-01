Col=[]
file = open('sample.txt', 'r')

for line in file:
    line=line.strip('\n')
    line=(line.split(' '))
    print (line[1])

