import sys

n = int(sys.stdin.readline())

ropeweight = []

for i in range(n):
    ropeweight.append(int(sys.stdin.readline()))


ropeweight.sort()
##print(ropeweight)

result = 0

for i in range(n):
##    print(ropeweight[i]*(n-i))
    result = max(result, ropeweight[i]*(n-i))

print(result)
