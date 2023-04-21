import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin = []
cnt = 0

for i in range(N):
    coin.append(int(input()))

coin = sorted(coin, reverse=True)

for i in coin:
    if K == 0:
        break
    cnt += K//i
    K %= i

print(cnt)