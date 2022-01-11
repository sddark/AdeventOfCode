# read in file lines
file1 = open('file.txt', 'r')
lines = file1.readlines()
arr1 = [1,1,1,1,1]
arr2 = [0,0,0,0,0]
gamma = epsilon = 0

print(len(lines))
for i in range(0, 4):
    count1 = count0 = 0

    for line in lines:
        filter = True

        if i > 1:
            for j in range(0, i):
                if int(line[j]) != arr1[j] & filter == True:
                    filter = False
        elif i == 1:
            if int(line[0]) != arr1[0] & filter == True:
                    filter = False
        
        if filter == True:

            if int(line[i]) == 1:
                count1 += 1
            else:
                count0 += 1

    if count1 > count0:
        arr1[i] = 1
    else:
        arr1[i] = 0

for i in range(0, 4):
    count1 = count0 = 0

    for line in lines:
        filter = True

        if i > 1:
            for j in range(0, i):
                if filter == True:
                    if int(line[j]) != arr2[j]:
                        filter = False
        elif i == 1:
            if int(line[0]) != arr2[0]:
                    filter = False
        
        if filter == True:

            if int(line[i]) == 1:
                count1 += 1
            else:
                count0 += 1

    if count1 < count0:
        arr2[i] = 1
    elif count1 == 1 & count0 ==1:
        break
    else:
        arr2[i] = 0

print(arr1) 
print(arr2) 

for i in range(0, len(arr1)):
    if arr1[i] == 1:
        gamma += 2 ** (11-i)

for i in range(0, len(arr2)):
    if arr2[i] == 1:
        epsilon += 2 ** (11-i)

print(gamma*epsilon)