N, M = map(int, input().split())

chessboard = []
result = []

for i in range(N):
    chessboard.append(input())

for i in range(N-7):
    for j in range(M-7):
        W = 0
        B = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if chessboard[k][l] != 'W':
                        W = W+1
                    if chessboard[k][l] != 'B':
                        B = B+1
                else:
                    if chessboard[k][l] != 'W':
                        B = B+1
                    if chessboard[k][l] != 'B':
                        W = W+1
        result.append(W)
        result.append(B)

print(min(result))