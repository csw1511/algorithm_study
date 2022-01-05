import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    d = []
    for i in range(n):
        a, b = map(int, input().split())
        d.append((a, b))


    d.sort()
    count = 1
    mini = d[0][1]
    for i in range(1, n):
        if d[i][1] < mini:
            mini = d[i][1]
            count += 1

    print(count)
