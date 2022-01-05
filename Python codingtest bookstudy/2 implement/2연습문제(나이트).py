a = input()

a = a.replace(a[0], str(ord(a[0])-96))

count = 0

x = int(a[0])
y = int(a[1])

pluma = [1,-1]
pluma2 = [2, -2]

for i in pluma2:
    for j in pluma:
        if x + i >=1 and y + j>=1:
            count +=1

for i in pluma2:
    for j in pluma:
        if x + j >=1 and y + i>=1:
            count +=1


print(count)
