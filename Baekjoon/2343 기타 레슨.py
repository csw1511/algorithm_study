import copy

n, m = map(int, input().split())

num_arr = []

num_arr = list(map(int, input().split()))

num_sum = 0

for i in num_arr:
    num_sum += i

ideal_len = num_sum // m    ##이상적인 분절의 크기
print('first Ideal:', ideal_len)
sum_cut = 0     ##각 분절의 숫자합 크기
count = 0       ##분절 개수


while True:

    temparr = copy.deepcopy(num_arr)
    vtemp = 0
    
    while temparr:
        if vtemp > ideal_len:
            ideal_len = vtemp
            print('ideal is fixed:', ideal_len)
        while sum_cut + vtemp <= ideal_len:
            sum_cut = sum_cut + vtemp
            try:
                vtemp = temparr.pop()
                print('vtemp: ', vtemp)
                print('temparr:', temparr)
            except:
                break
        count += 1
        sum_cut = 0
        print('i am  look count: ', count)

        
    if count > m:
        ideal_len += 1
        print('-------------Ideal: ', ideal_len)
        count = 0
        continue
    if count == m:
        print('its done')
        break

print(ideal_len)
