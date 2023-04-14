import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
block = []

for i in range(N):
    block.append([int(j) for j in input().split()])

time = int(1e9)
height = 0

for i in range(257):  # 땅의 높이
    use = 0
    take = 0

    for j in range(N):
        for k in range(M):
            if block[j][k] > i:
                take += block[j][k] - i
            else:
                use += i - block[j][k]

    if use > take + B:
        continue

    cnt = take*2 + use

    if cnt <= time:
        time = cnt
        height = i

print(time, height)