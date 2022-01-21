n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(int(input()))

memoilist = [-1] * (100)

for i in arr:
    memoilist[i] = 1



for i in range(m+1):
    tmparr = []
    for j in arr:
        if i-j > 0:
            if memoilist[i-j] != -1:
                tmparr.append(memoilist[i-j]+1)
    if tmparr:
        memoilist[i] = min(tmparr)

print(memoilist[m])

"""
입력 예시
2 15
2
3
예상 출력
5

입력 예시
3 4
3
5
7
예상 출력
-1
"""


    