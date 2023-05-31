num = []
max_n, max_row, max_col = 0, 0, 0
for i in range(9):
    num.append(list(map(int, input().split())))
for i in range(9):
    for j in range(9):
        if max_n <= num[i][j]:
            max_n = num[i][j]
            max_row = i + 1
            max_col = j + 1
print(max_n)
print(max_row, max_col)