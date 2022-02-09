n = list(map(int, input()))


lenn = len(n)

Lsum = sum(n[:lenn//2])
Rsum = sum(n[lenn//2:])

if Lsum == Rsum :
    print("LUCKY")
else:
    print("READY")

