n = input()



def solution(p):
    result = []
    #if iscorrect(p):
    #    return p

    u, v = slicebracket(p)
    print(u)
    print(v)

    while iscorrect(u):
        for i in u:
            result.append(i)
        u, v = slicebracket(u)
        print(u)
        print(v)
    
    u.insert(0, '(')


    


#u와 v 생성기
def slicebracket(w):
    wlist = []

    for i in w:
        wlist.append(i)
    
    count = 0
    u = []
    v = []
    u.append(wlist[0])
    if wlist[0] == '(':
        count +=1
    elif wlist[0] == ')':
        count -=1
    del wlist[0]

    while count != 0:
        u.append(wlist[0])
        if wlist[0] == '(':
            count +=1
        elif wlist[0] == ')':
            count -=1
        del wlist[0]
    
    for i in wlist:
        v.append(i)
    return u, v

#올바른 배열인지 확인
def iscorrect(strr):
    strrlist = []

    for i in strr:
        strrlist.append(i)
    
    strrstack = []
    while strrlist:
        strrstack.append(strrlist[0])
        del strrlist[0]


        lenstack = len(strrstack)
        try:
            if strrstack[lenstack-2] == '(':
                if strrstack[lenstack-1] == ')':
                    del strrstack[lenstack-2]
                    del strrstack[lenstack-2]
        except:
            continue

    if strrstack:
        return False
    else:
        return True

print(solution(n))