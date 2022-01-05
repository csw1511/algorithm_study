n = int(input())

count_3 = 0

time = 0

time_limit = n * 10000 + 5959

while time != time_limit:
    if time%10000 > 5959 or time%100 > 59:
        time += 1
        continue
    
    if str(time).count('3'):
        count_3 += 1
    time += 1

print(count_3)
