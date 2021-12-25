import sys

n = str(sys.stdin.readline())


result = 0


n = n.split('-')

firsttemp = []
firsttemp = n[0].split('+')

for i in firsttemp:
    result += int(i)


for i in n[1:]:
    i = i.split('+')
    for j in i:
        j = int(j)
        result -= j
print(result)
