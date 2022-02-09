def solution(key, lock):
    answer = True
    def rclock90(key):
        key90=[]
        for i in key:
            key90.append(i[:])
        lenkey = len(key90)
        for i in range(lenkey):
            for j in range(lenkey):
                key[i][j] = key90[j][lenkey-1-i]
    
    for i in key:
        print(i)

    for i in lock:
        print(i)

    
    lenkey = len(key)
    for _ in range(4):
        tmplock = lock[:]
        for i in range(lenkey):
            for j in range(lenkey):
                for a in range(i):
                    for b in range(j):
                        tmplock[a][b] += key[a][b]
                if tmplock == [[1,1,1],[1,1,1],[1,1,1]]:
                    return tmplock
        rclock90(key)
            

                


    return answer

key = input()
lock = input()


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))



"""
for i in tmplock:
                    print(i)
                print("---")
[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
[[1, 1, 1], [1, 1, 0], [1, 0, 1]]
"""