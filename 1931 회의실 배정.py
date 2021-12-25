n = int(input())

dislist = []

for i in range(n):
    start, end = map(int, input().split())
    dislist.append((start, end))
    
    
def timetable(dislist):    
    list_start = sorted(dislist)

    lastdis = list_start.pop()
    count = 1
    
    while list_start:
        temp = list_start.pop()
        if temp[1] > lastdis[0]:    ##temp의 끝이 lastdis의 시작보다 더 느리면
            continue
        count +=1
        lastdis = temp  ##왜? 조건에 합격한 temp가 앞으로의 lastdis가 되어야 함

    return count

print(timetable(dislist))
