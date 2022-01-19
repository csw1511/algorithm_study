n = int(input())

arrn = list(map(int, input().split()))

m = int(input())

arrm = list(map(int, input().split()))

def binsear(arr, target, start, end):
    if start > end:
        return False;

    middle = (start + end)//2
    if arr[middle] == target:
        return True
    
    elif arr[middle] > target:
        return binsear(arr,target,start,middle-1)
    else:
        return binsear(arr,target,middle+1,end)


arrn.sort()
print(arrn)

for i in arrm:
    if binsear(arrn, i, 0, n-1) == True:
        print('yes', end=' ')
    else:
        print('no', end=' ')

"""
입력 예시
5
8 3 7 9 2  
10
0 1 2 3 4 5 6 7 8 9
예상 출력 
[2, 3, 7, 8, 9]
no no yes yes no no no yes yes yes
"""
