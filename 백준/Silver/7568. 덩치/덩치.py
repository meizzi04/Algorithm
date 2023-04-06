N = int(input())
num = []
result = []

for i in range(N):
    num.append(list(map(int, input().split())))

for i in num:
    rank = 1
    for j in num:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')