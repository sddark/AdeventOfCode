with open('file.txt', 'r') as file:
    crab = [int(number) for number in file.readline().split(',')]

max1 = max(crab)
min1 = min(crab)

print(min1,' : ', max1)
for i in range(min1, max1):
    cost = 0
    for j in range(0, len(crab)):
        distance = abs(i - crab[j])
        cost += distance * (distance + 1) / 2
    if i == min1:
        lowestcost = cost
    elif cost < lowestcost:
        lowestcost = cost
    else:
        break

print(lowestcost)

