# steps to complete bingo
# 1 print out row of first board in integers
# 2 print out columns of first board in integers
# 3 loop through row to determine if it has all 5
# 4 loop through column to determine if it has all 5
# 5 when winning board is found loop through multiply all non selected together

file1 = open('file.txt', 'r')
sample = file1.readlines()
lines = []
numberin = False
winner = False
counttrues = 0

for line in sample:
    lines.append(line.strip('\n'))
    print(line)


numboards = int((len(lines)-1)/6)
called = lines[0].split(',')
print(called)

print(lines[0][1])
#number of guesses
for count in range(5, len(called)):
    #boards
    for l in range(0, numboards):
        #rows
        for j in range(l*5+0,l*5+5):
            if counttrues == 5:
                winner = True
                break

            counttrues = 0
            for i in range(0,):
                if lines[j+2][i*3] == ' ':
                    number = lines[j+2][i*3+1]
                else:
                    number = lines[j+2][i*3]+lines[j+2][i*3+1]
                
                numberin = False
                for k in range(0,count):
                    print(called[k])
                    print(number)
                    if called[k] == number:
                        numberin = True
                        print(number)
                        break
                
                if numberin == True:
                    counttrues += 1

        #columns 
        for j in range(0,5):
            if counttrues ==5:
                winner = True
                break

            counttrues = 0
            for i in range(l*5+0,l*5+5):
                print(i+2)
                if lines[i+2][j*3] == ' ':
                    number = lines[i+2][j*3+1]
                else:
                    number = lines[i+2][j*3]+lines[i+2][j*3+1]

                numberin = False
                for k in range(0,count):
                    print(called[k])
                    print(number)
                    if called[k] == number:
                        numberin = True
                        print(number)
                        break
                
                if numberin == True:
                    counttrues += 1
            


#
#for line in lines:
#    line.strip('\n')
#    print(line)