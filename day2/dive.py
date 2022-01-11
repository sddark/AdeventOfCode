# read in file lines
file1 = open('file.txt', 'r')
lines = file1.readlines()

# initialize variables
aim = 0
depth = 0
horizontal = 0

# determine direction based off of first letter and last char(-2) 
# since there is a return carriage
for line in lines:
    if line[0] == 'f':
        depth += float(line[-2]) * aim
        horizontal += float(line[-2])
    elif line[0] == 'd':
        aim += float(line[-2])
    else:
        aim -= float(line[-2])

#print stuff
print(horizontal * depth)