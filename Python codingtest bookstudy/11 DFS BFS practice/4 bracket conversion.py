
n = input()



def solution(p):
    result = []
    string = ''.join(makeresult(p, result))
    return string

def makeresult(p, result):
    if p == []:
        return result

    u, v = slicebracket(p)

    if iscorrect(u):
        for i in u:
            result.append(i)
        
        return makeresult(v, result)
    else:
        resultt =['(']
        tmpv = makeresult(v, [])
        for i in tmpv:
            resultt.append(i)
        resultt.append(')')

        for i in range(1, len(u)-1):
            if u[i] == ')':
                resultt.append('(')
            elif u[i] == '(':
                resultt.append(')')
        
        result.extend(resultt)
        return result

#u와 v 생성기
def slicebracket(w):
    if w ==[]:
        return w, w
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

#u, v = slicebracket(n)
#print(slicebracket(v))
print(solution(n))
