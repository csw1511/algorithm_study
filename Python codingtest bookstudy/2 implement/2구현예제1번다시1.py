n = int(input())

horizon = 1
vertical = 1

arr = list(map(str, input().split()))

for i in arr:
    if i == 'R':
        horizon += 1
        if horizon > 5:
            horizon -= 1
    elif i == 'L':
        horizon -= 1
        if horizon < 1:
            horizon += 1
    elif i == 'U':
        vertical -= 1
        if vertical < 1:
            vertical += 1
    elif i == 'D':
        vertical += 1
        if vertical > 5:
            vertical -=1

print(vertical,horizon)
