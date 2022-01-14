n,m = map(int, input().split())

a, b, d = map(int, input().split())

mapmap = []
for i in range(n):
    tmplist = list(map(int, input().split()))
    mapmap.append(tmplist)



#0번 인덱스부터 차례대로 북, 서, 남, 동
hor = [-1, 0, 1, 0]
ver = [0, -1, 0, 1]

#육지 = 0
#바다 = 1
#캐릭터가 현재 있는 위치 = 2
#이미 가본 육지 = -1
mapmap[a][b] = 2
while True:
    # 더이상 움직일 수 없는가?
    isend = False
    #반시계 방향으로 둘러보기. 최대 4번임
    for aaa in range(4):
        # 캐릭터 보는방향 반시계로 한칸 움직이기
        d = d+1
        d = d%4
        #이후 캐릭터 보는 방향이 아직 안가본 땅이라면 캐릭터를 움직이고
        #해당 칸에 맞는 번호 부여하기. 그리고 배열 나가서 다시 시작하기
        if mapmap[a+hor[d]][b+ver[d]] == 0:
            mapmap[a][b] = -1
            mapmap[a+hor[d]][b+ver[d]] = 2
            a = a + hor[d]
            b = b+ver[d]
            break;
        #만약 네 방향 다 가본 땅이거나 갈수없는 땅이라면
        if aaa == 3:
            # 캐릭터의 뒤쪽 방향을 지정하고(보는방향 유지를 위해 tmp변수를 사용)
            tmp = d + 2
            tmp = tmp%4
            # 뒤로 한칸 움직이고 해당 칸에 맞는 번호 부여하기
            #여기서 만약 뒤가 바다 칸(1)이라면 더이상 움직일수 없다 판단하고 while문 종료
            if mapmap[a+hor[tmp]][b+ver[tmp]] == 1:
                isend = True
                break;
            mapmap[a][b] = -1
            mapmap[a+hor[tmp]][b+ver[tmp]] = 2
            a = a + hor[tmp]
            b = b+ver[tmp]
    #while문 종료
    if isend :
        break

#최종 맵 모양 확인용
for i in mapmap:
    print(i)

#문제에서 원하는 답 출력을 위해 맵 전체를 둘러보며 캐릭터가 족적을 남긴 땅 갯수 세기
count =0
for i in mapmap:
    for j in i:
        if j == -1 or j == 2:
            count += 1

    
print(count)


"""
입력 예시
6 6
1 1 0
1 1 1 1 1 1
1 0 0 0 0 1
1 1 0 0 0 1
1 1 0 1 0 1
1 0 0 1 0 1
1 1 1 1 1 1

4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""


