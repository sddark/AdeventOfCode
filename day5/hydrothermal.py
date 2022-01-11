file1 = open('file.txt', 'r')
sample = file1.readlines()
lines = []
test = []
test2 = []
# initialize that map
map1 = [[0 for c in range(1000)] for r in range(1000)]

# parse the data
for line in sample:
    test.append(line.strip('\n'))
    
for line in test:
    test2.append(line.split(' -> '))

for line in test2:
    for i in range(0, len(line)):
        lines.append(line[i].split(','))

for i in range(0, int(len(lines)/2)):
    x1 = int(lines[2*i][0])
    x2 = int(lines[2*i+1][0])
    y1 = int(lines[2*i][1])
    y2 = int(lines[2*i+1][1])

    xdif = int(abs(x2 - x1))
    ydif = int(abs(y2 - y1))

    if y1 == y2:
        for x in range(0, xdif+1):
            if x2 > x1:
                map1[y1][x1 + x] += 1
            else:
                map1[y1][x1 - x] += 1
    elif x1 == x2:
        for y in range(0,ydif+1):
            if y2 > y1:
                map1[y1 + y][x1] += 1
            else:
                map1[y1 - y][x1] += 1
    else:
        for d in range(0, xdif+1):
            if x2 > x1 and y2 > y1:
                map1[y1 + d][x1 + d] += 1
            elif x2 < x1 and y2 > y1:
                map1[y1 + d][x1 - d] += 1
            elif x2 > x1 and y2 < y1:
                print(x1 + d)
                map1[y1 - d][x1 + d] += 1
            else:
                map1[y1 - d][x1 - d] += 1
            

    

count = 0
for x in range(0, 1000):
    for y in range(1,1000):
        if map1[y][x] > 1:
            count +=1
            print('X:', x, ' Y: ', y)
print(count)
#for line in map1:
#    print(line , '\n')

            


    
    

