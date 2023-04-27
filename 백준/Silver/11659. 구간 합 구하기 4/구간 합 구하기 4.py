import sys
input = sys.stdin.readline

N, M = map(int, input().split())

num = list(map(int, input().split()))
result = [0]
sum = 0

for i in num:
    sum += i
    result.append(sum)

for m in range(M):
    i, j = map(int, input().split())

    print(result[j]-result[i-1])