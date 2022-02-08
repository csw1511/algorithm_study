
food_times=list(map(int,input().split()))

k = int(input())
lenfoodtime = len(food_times)

eated = k // lenfoodtime
eatable = k % lenfoodtime


for i in range(lenfoodtime):
    food_times[i] -= eated

print(food_times)

resultfind = 0
iterd = 0

while eatable != 0:
    if food_times[iterd] != 0:
        food_times[iterd] -= 1
        eatable -= 1
    iterd += 1

print(food_times, iterd)
if iterd - lenfoodtime >= 0:
    iterd = iterd - lenfoodtime

for _ in range(lenfoodtime):
    if food_times[iterd] != 0:
        print(iterd+1)
        break
    iterd += 1
    if iterd == lenfoodtime-1:
        iterd = 0

