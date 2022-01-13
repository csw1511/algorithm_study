n = int(input())

h = 0
m = 0
s = 0

count =0
while h != n or m != 59 or s != 59:
    s += 1
    if s == 60:
        s = 0
        m += 1
    if m == 60:
        m = 0
        h += 1
    if '3' in str(s) + str(m) + str(h):
        count += 1

print(count)