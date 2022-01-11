coords = [list(i) for i in open('file.txt', 'r').read().strip().splitlines()]
print(coords)

risk = 0
for x in range(0, len(coords)):
    for y in range(0, len(coords[x])):

        lowest = True
        if x >= 1:
            if coords[x][y] >= coords[x-1][y]:
                lowest = False
        if x < len(coords) - 1:
            if coords[x][y] >= coords[x+1][y]:
                lowest = False
        if y >= 1:
            if coords[x][y] >= coords[x][y-1]:
                lowest = False
        if y < len(coords[x]) - 1:
            if coords[x][y] >= coords[x][y+1]:
                lowest = False

        if lowest == True:
            risk += int(coords[x][y]) + 1
            print('x:',x,'y',y,int(coords[x][y]))
            #print(coords[x][y])

print(risk)