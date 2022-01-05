n = int(input())

numarr = []

for _ in range(n):
    temp = list(map(str, input()))
    temp.reverse()
    numarr.append(temp)

numarr.sort(key=len, reverse = True)

print(numarr)#

numatlist = [[] for i in range(len(numarr[0]))]
print(numatlist)#

for j in range(len(numarr[0])):
    try:
        for i in numarr:
            i.reverse()
            numatlist[j].append(i.pop())
            i.reverse()
    except:
        continue

numatlist.reverse()
print(numatlist)#

numlist = [0,1,2,3,4,5,6,7,8,9]

numdic = {}
numvis = [0]*26

for i in numatlist:
    temp = []
    while i:
        itmp = i.pop()
        temp.append(itmp)
        if numvis[ord(itmp)-65] == 0:
            numvis[ord(itmp)-65] += 1
            numdic[itmp] = numlist.pop()
    while temp:
        i.append(temp.pop())

print(numdic)#
print(numatlist)#

result = 0

for i in range(len(numatlist)):
    while numatlist[i]:
        result += numdic[numatlist[i].pop()] *(10** (len(numatlist) - i - 1))

print(result)
    
##실패이유: 빈도가 높은 숫자는 그렇지 않은 숫자와 같은 자릿수에서 등장하더라도 더 큰 숫자가 부여되어야
##함을 알지 못했다. 이를 내 코드를 수정하여 해결할 방식이 딱히 떠오르지 않는다
