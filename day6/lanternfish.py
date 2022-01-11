with open('file.txt', 'r') as file:
    fish = [int(number) for number in file.readline().split(',')]

count = 0
fishlife = [0, 0, 0, 0, 0, 0, 0, 0, 0]
day = 0

for i in range(0, len(fish)):
    fishlife[fish[i]] += 1

while day < 256:
    day += 1
    temp = fishlife[0]

    for i in range(0, len(fishlife)-1):
        fishlife[i] = fishlife[i+1]

    fishlife[6] += temp
    fishlife[8] = 0
    fishlife[8] += temp    

for i in range(0, len(fishlife)):
    count += fishlife[i]

print(count)

