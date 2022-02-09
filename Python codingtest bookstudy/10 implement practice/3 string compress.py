def solution(s):
    answer = 0
    lens = len(s)
    
    answer = lens
    
    for j in range(1, lens//2 + 1):
        count = 1
        tmparr = []
        for i in range(0, lens, j):
            try:
                tmpstr = [[],[]]
                for p in range(j):
                    tmpstr[0].append(s[i+p])
                for p in range(j):
                    tmpstr[1].append(s[i+j+p])

                if tmpstr[0] == tmpstr[1]:
                    count += 1
                if tmpstr[0] != tmpstr[1]:
                    if count > 1:
                        countlen = len(str(count))
                        for _ in range(countlen):
                            tmparr.append(count)
                    for ppp in tmpstr[0]:
                        tmparr.append(ppp)
                    count = 1
            except:
                if count > 1:
                    countlen = len(str(count))
                    for _ in range(countlen):
                        tmparr.append(count)
                for ppp in tmpstr[0]:
                    tmparr.append(ppp)
                count = 1

        answer = min(answer, len(tmparr))
    return answer

s = str(input())

print(solution(s))


"""
"aaaaaaaaaaaabcd" -> 6
"6aabcd

"xxxxxxxxxxyyy" -> 5
"""