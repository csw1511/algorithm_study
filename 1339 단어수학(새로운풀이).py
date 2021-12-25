n = int(input())

numarr = []

for _ in range(n):
    temp = list(map(str, input()))
    temp.reverse()
    numarr.append(temp)

numarr.sort(key=len, reverse=True)

numdic ={}
for i in range(26):
    numdic[chr(65+i)] = 0
    

for i in numarr:
    for j in range(len(numarr[0])):
        try:
            numdic[i[j]] += 10 ** j
        except:
            continue

numlist = [0,1,2,3,4,5,6,7,8,9]

##print(numdic)

key_max = max(numdic, key=lambda k: numdic[k])
##print(key_max)
##print(numdic[key_max])
##print(numlist.pop())
result = 0
while numdic[key_max] != 0:
    tmp = numlist.pop()
    result += numdic[key_max] * tmp
    numdic[key_max] = 0
    key_max = max(numdic, key=lambda k: numdic[k])
    

print(result)

