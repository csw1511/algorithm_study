n = int(input())

arr = list(map(int,input().split()))

memoilist = [0] * (n)

memoilist[0] = arr[0]

memoilist[1] = max(arr[0], arr[1])

for i in range(2, n):
    memoilist[i] = max(memoilist[i-1], memoilist[i-2] + arr[i])

print(memoilist) 
print(memoilist[n-1])

"""
입력 예시 
4
1 3 1 5
예상 출력
[1, 4, 4, 8]
8

입력 예시
10
1 6 4 2 9 8 3 5 9 3
예상 출력
[1, 7, 10, 10, 15, 17, 17, 17, 18, 18]
18
"""