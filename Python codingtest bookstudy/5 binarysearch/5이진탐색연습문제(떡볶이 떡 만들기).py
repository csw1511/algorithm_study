n, m= map(int, input().split())

arr = list(map(int, input().split()))

def mass_of_dduk(arr, length, m):
    sum = 0
    for i in arr:
        if (i - length)>=0:
            sum += (i-length)
    if sum >= m:
        return True
    else:
        return False


def binsearch(arr, m):
    left = 0
    right = max(arr)
    while left <= right:
        mid = (left + right)//2
        if mass_of_dduk(arr, mid, m):
            left = mid + 1
        else:
            right = mid - 1

    return (left + right)//2

##파라메트릭 서치에서 이러한 형태의 binsearch는 다음과 같이 동작한다
##어떠한 조건 기준으로 만족(왼쪽) / 불만족(오른쪽)으로 가를 수 있다고 할때
##조건에 마지막으로 부합하는 최댓값에는 right, (left + right)//2가 위치하고
##조건에 처음으로 부합하지 않는 최솟값에는 left가 위치한다
##파라메트릭 서치의 목적에 맞게 이를 조절하여 return할 줄 알아야 한다

print(binsearch(arr, m))

print(mass_of_dduk(arr,15,6))
##여기서 그 특성이 드러나는데, 절단기 길이에 따라 남은 떡이 주어진 m에 부합하
##는지 여부를 확인하는 함수에서는 절단기 길이가 15일때 합격판정을 내려준다
##하지만 binsearch 에서 마지막 return을 left로 하면 바로 다음인 16을 값으로
##돌려주게 된다.
