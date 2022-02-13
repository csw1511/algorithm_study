n = int(input())

k = int(input())

matrix = [[0]*(n) for i in range(n)]

for _ in range(k):
    row, col = map(int,input().split())
    matrix[row-1][col-1] = 1

l = int(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]


going = []
for _ in range(l):
    go, turn = map(str, input().split())
    going.append([int(go), turn])

for i in range(len(going)-1, 0, -1):
    going[i][0] -= going[i-1][0]

going.append([10000,'A'])

    
snakehead = [0,0]
snaketail = [0,0]
snakedirect = 0
matrix[0][0] = 2

count = 0
isEnd = False

for i in going:
    go, turn = i
    for _ in range(go):
        snakehead[0] += dx[snakedirect]
        snakehead[1] += dy[snakedirect]
        if snakehead[0] == n or snakehead[0] == -1 or snakehead[1] == n or snakehead[1] == -1:
            count += 1
            isEnd= True
            break
        if matrix[snakehead[0]][snakehead[1]] == 2:
            count += 1
            isEnd= True
            break
        savedmatrix = matrix[snakehead[0]][snakehead[1]]
        matrix[snakehead[0]][snakehead[1]] = 2

        if savedmatrix == 0:
            matrix[snaketail[0]][snaketail[1]] = 0
            for t in range(4):
                tailnext = [snaketail[0] + dx[t], snaketail[1] + dy[t]]
                if tailnext[0] == n or tailnext[0] == -1 or tailnext[1] == n or tailnext[1] == -1:
                    if t == 3:
                        snaketail[0] += dx[snakedirect]
                        snaketail[1] += dy[snakedirect]
                    continue
                if matrix[tailnext[0]][tailnext[1]] == 2:
                    snaketail[0] = tailnext[0]
                    snaketail[1] = tailnext[1]
                    break
                if t == 3:
                    snaketail[0] += dx[snakedirect]
                    snaketail[1] += dy[snakedirect]
        for i in matrix:
            print(i)
        print('---')
        print(snakehead, snaketail)
        count += 1
       
        
    if isEnd:
        print(count)
        break
    
    if turn == 'D':
        snakedirect = (snakedirect + 1) % 4
    elif turn == 'L':
        snakedirect = (snakedirect - 1) % 4
    print(snakedirect)



"""

6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
9

10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L
21

10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
13

58
58
31 50
13 34
54 27
21 40
17 36
28 48
38 27
13 51
53 44
28 57
10 25
26 20
29 31
2 6
53 24
19 45
31 58
30 36
2 33
52 31
22 30
15 56
44 36
26 12
47 18
10 57
4 5
28 52
6 30
48 15
5 38
25 38
29 48
50 40
36 5
35 15
45 9
56 42
18 15
51 9
33 29
26 47
46 28
43 29
16 41
16 30
38 35
49 14
20 7
39 50
21 36
40 25
9 5
6 4
49 23
15 32
41 4
42 2
78
5 D
8 D
10 L
15 L
17 L
18 L
20 L
32 L
64 D
65 L
76 D
81 L
82 D
86 L
87 D
88 L
91 L
94 D
100 D
103 D
107 D
109 L
110 D
111 D
115 D
116 L
117 D
118 D
119 L
120 L
121 D
143 D
192 D
229 D
276 L
287 L
313 L
365 D
366 D
403 L
404 L
439 D
440 D
463 L
464 L
469 D
470 L
482 D
493 D
494 D
498 L
510 L
513 D
514 L
519 L
520 D
529 L
545 L
552 D
558 D
564 D
565 D
568 L
570 L
574 D
576 D
581 D
588 D
597 D
619 D
672 D
678 D
693 D
742 L
743 L
747 D
748 L
751 L
"""