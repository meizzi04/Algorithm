import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin = []
cnt = 0

for i in range(N):
    coin.append(int(input()))

coin = sorted(coin, reverse=True)

for i in coin:
    if i > K:
        continue
    else:
        while i <= K:
            K -= i
            cnt += 1

print(cnt)