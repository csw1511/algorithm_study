import sys

b = int(sys.stdin.readline())


n = 1000 - b


coin_list = [500, 100, 50, 10, 5, 1]
count = 0


for i in coin_list:
    if n == 0:
        break
    count = count + n // i
    if n >= i:
        n = n % i

print(count)
