n = int(input())

arr = list(map(int, input().split()))

"""
min1 - 가장 작은 수를 가진 주사위의 면
min2 - 가장 작은 수 합을 가지는 주사위의 모서리
min3 - 가장 작은 수 합을 가지는 주사위의 꼭짓점

주사위로 이루어지는 정육면체의 바깥 네 꼭짓점을 min3이 구성하고
정육면체의 옆면 모서리 4개와 윗면 모서리 4개를 min2이 구성하고
나머지 정육면체의 면을 min1이 구성한다
"""
min1 = min(arr)
min2 = 1000

for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if i + j == 5:
            continue
        summ = arr[i] + arr[j]
        if summ < min2:
            min2 = summ

mincd = min(arr[2], arr[3])
ab = arr[0]+arr[1]
ae = arr[0]+arr[4]
fb = arr[5]+arr[1]
fe = arr[5]+arr[4]
minabef = min(ab, ae, fb, fe)
min3 = minabef + mincd
## 여기까지 min1, 2, 3을 구하는 과정

#구한 min1, 2, 3을 정육면체 구성에 필요한 수만큼 곱하여 모두 더함
result = min1 * (5*n**2 - 16*n + 12) + min2*(8*n - 12) + min3*4

#예외로 n이 1일경우 위 공식이 적용되지 않으므로, 가장 큰 수를 제외하여 나머지 5면의 합을 정답으로 함
if(n==1):
    result = sum(arr)-max(arr)
print(result)

"""
타인의 답안을 보고 배운 점
: 주사위는 6면이고 한 면과 맞닿아있지 않은 면은 한개뿐이다
따라서 위의 min1, 2, 3을 구할때
마주보는 면인 a - f, b - e, c - d끼리 비교하여
더 작은 면만을 취한다면 이 면들은 반드시 서로 맞닿아있게 된다
이들 자체를 그대로 사용하되, 정육면체 면 더하는 공식을 약간 바꾸어 적용할 수 있을 것이다.
아니면 이들을 이용하여 위와 같이 반복문을 돌리거나, 직접 면들을 구하는 귀찮은 과정 없이
min1, 2, 3을 구할 수 있을 것이다
"""