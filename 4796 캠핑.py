count = 1

while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    ahrttn = v // p
    skajwl = v % p
    if skajwl > l:
        skajwl = l

    result = (ahrttn * l) + skajwl
    
    print("Case", str(count) + ":", result)
    count += 1
