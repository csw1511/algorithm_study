from itertools import combinations

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))


#주어진 상황에서 치킨거리의 최솟값 구하는 함수
def minchick(listhome, listchick):
    result = 0
    for i in listhome:
        temp = int(1e9)
        for j in listchick:
            temp =  min(temp, abs(i[0]-j[0]) + abs(i[1]-j[1]))
        result += temp
    
    return result

#집들의 위치
lochome = []

#치킨집의 위치
locchick = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            lochome.append((i, j))
        elif graph[i][j] == 2:
            locchick.append((i,j))

##print(lochome)
##print(locchick)

Mlocchick = []

for i in combinations(locchick, m):
    tmp = list(i)
    Mlocchick.append(tmp)
##print(Mlocchick)

answer = int(1e9)


for i in Mlocchick:
    tmp = minchick(lochome, i)
    answer = min(answer, tmp)

print(answer)
