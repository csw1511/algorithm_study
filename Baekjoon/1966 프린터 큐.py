from collections import deque

testcase = int(input())


while(testcase != 0):

    n, m = map(int, input().split())

    impo = deque(list(map(int,input().split())))
    count = 0 #어떤 한 문서 m이 몇번째로 인쇄되는지 세는 변수
    while(m != -1): #m번째 문서가 출력되는 순간의 조건
        maximpo = max(impo) # 리스트의 최대우선순위
        tmp = impo.popleft() # 리스트 맨 앞 값을 가져온다
        if(tmp < maximpo): # 이게 최대우선순위가 아니라면
            impo.append(tmp) # 다시 맨 뒤로 보내고
            if m != 0: # 이때 m번째 문서의 순서를 조정한다
                m -= 1
            else:
                m = n-1
        else: # 만약 이게 최대우선순위 문서라면
            count += 1 # 그대로 리스트에서 값을 빼버리고, 카운트를 하나 올린다
            n -= 1 # 리스트 크기가 줄어들었으므로 리스트크기를 조정한다
            m -= 1 # 마찬가지로 m번째 문서의 순서를 조정한다. 이때 m문서가 0번째여서 -1이라면 반복문이 끝난다
            
    print(count) # m문서가 출력된 순서를 출력
    
    

    testcase -= 1

