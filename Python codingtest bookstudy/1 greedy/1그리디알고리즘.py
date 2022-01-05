n = int(input())

Num500 = 0
Num100 = 0
Num50 = 0
Num10 = 0

if n>=500:
    Num500 = int(n/500)
    n = n%500
if n>=100:
    Num100 = int(n/100)
    n = n%100
if n>=50:
    Num50 = int(n/50)
    n = n%50
if n>=10:
    Num10 = int(n/10)
    n = n%10



print(Num500 + Num100 + Num50 + Num10)

