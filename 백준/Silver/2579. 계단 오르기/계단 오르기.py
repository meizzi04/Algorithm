N = int(input())
stairs = []

for i in range(N):
    stairs.append(int(input()))

dp = [0]*N

if len(stairs) <= 2:
    print(sum(stairs))
else:
    dp[0] = stairs[0]
    dp[1] = stairs[0]+stairs[1]

    for i in range(2, N):
        dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
    print(dp[-1])