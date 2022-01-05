def moveset(M):
    if M == 'L':
        return (0, -1)
    elif M == 'R':
        return (0, 1)
    elif M == 'U':
        return (-1, 0)
    elif M == 'D':
        return (1, 0)

Size_arr = int(input())

moving = input().split()

traver1 = 1
traver2 = 1

for i in moving:
    a = moveset(i)[0]
    b = moveset(i)[1]
    if (traver1 + a >=1) and (traver1 + a <=Size_arr):
        traver1 += a
    if (traver2 + b >=1) and (traver2 + b <=Size_arr):
        traver2 += b
print(traver1, traver2)

