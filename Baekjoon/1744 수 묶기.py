n = int(input())

forplus = []
for0 = []
forminus = []

result = 0

for i in range(n):
    tmp = int(input())
    if tmp == 1:
        result += 1
    elif tmp == 0:
        for0.append(tmp)
    elif tmp < 0:
        forminus.append(tmp)
    else:
        forplus.append(tmp)

forplus.sort()
forminus.sort(reverse = True)

while forplus:
    tmp1 = forplus.pop()
    try:
        tmp2 = forplus.pop()
    except:
        result += tmp1
        break
    result += tmp1 * tmp2

while forminus:
    tmp1 = forminus.pop()
    try:
        tmp2 = forminus.pop()
    except:
        if for0:
            break
        else:
            result += tmp1
            break
    result += tmp1 * tmp2

print(result)
