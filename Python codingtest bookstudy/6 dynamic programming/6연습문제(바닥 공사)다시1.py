n = int(input())

memoilist = [0]*(n+1)

memoilist[1] = 1
memoilist[2] = 3

for i in range(3, n+1):
    memoilist[i] = memoilist[i-1] + memoilist[i-2]*2

print(memoilist)

tmp = memoilist[n] % 796796
print(tmp)
"""
입력 예시
3
예상 출력
[0, 1, 3, 5]
5

입력 예시
10
예상 출력
[0, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683]
683
"""