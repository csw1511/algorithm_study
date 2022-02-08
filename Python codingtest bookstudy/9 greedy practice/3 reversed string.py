arr = input()

print(arr)

arr0 = arr.split('1')
arr1 = arr.split('0')

count0 = 0
count1 = 0

for i in arr0:
    if i != '':
        count0 += 1

for i in arr1:
    if i != '':
        count1 += 1


print(min(count0, count1))