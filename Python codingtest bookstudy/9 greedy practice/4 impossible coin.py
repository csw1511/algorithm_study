from turtle import Turtle


n = int(input())
arr = list(map(int, input().split()))


arr.sort(reverse=True)

impossiblecoin = sum(arr) + 1

def find():

    for i in range(impossiblecoin-1, 0, -1):
        for j in arr:
            i -= j
            if i == 0:
                break
            if i < 0:
                if j == arr[0]:
                    return (i+j)
                i += j
                continue
            
print(find())