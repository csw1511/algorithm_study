n = list(map(str, input()))

n.sort()

tmpint = []
tmpstr = []

for i in n:
    try:
        tmpint.append(int(i))
    except:
        tmpstr.append(i)
        
result = tmpstr + tmpint

for i in result:
    print(i, end='')