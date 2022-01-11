file1 = open('file.txt', 'r')
sample = file1.readlines()

lines = []
test = []
test2 = []

for line in sample:
    test.append(line.strip('\n'))

for line in test:
    test2.append(line.split(' | '))

for line in test2:
    for i in range(0, len(line)):
        lines.append(line[i].split(' '))

#print(lines)
#print(len(lines))
count = 0
for i in range(0 , int(len(lines)/2)):
    for j in range(0, len(lines[i*2+1])):
        if len(lines[i*2+1][j]) == 2 or len(lines[i*2+1][j]) == 3 or len(lines[i*2+1][j]) == 4 or len(lines[i*2+1][j]) == 7:
            count += 1
print(count)
