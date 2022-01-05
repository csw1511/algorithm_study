n, k = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse= True)

for i in range(k):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]

AnsSum = 0

for i in A:
    AnsSum += i

print(AnsSum)
