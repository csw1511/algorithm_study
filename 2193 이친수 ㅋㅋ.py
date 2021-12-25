import sys
input = sys.stdin.readline

n = int(input())

d = [0]*(n+1)

d[1] = 1

ifNis1 = False

try:
    d[2] = 1

    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2]
except:
    ifNis1 = True
    print(d[1])

if ifNis1 == False:
    print(d[n])

