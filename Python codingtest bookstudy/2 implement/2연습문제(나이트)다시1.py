n = input()
hor = int(ord(n[0])) - int(ord('a')) +1
ver = int(n[1])


hormove = [2, 2,-2,-2,1,1,-1,-1]
vermove = [1, -1,1,-1,2,-2,2,-2]

count = 0
for i in range(8):
    hortmp = hor + hormove[i]
    vertmp = ver + vermove[i]
    if hortmp > 8 or hortmp < 1 or vertmp > 8 or vertmp < 1:
        continue
    count += 1

print(count)