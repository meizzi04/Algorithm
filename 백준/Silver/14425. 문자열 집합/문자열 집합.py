import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = set()
cnt = 0

for i in range(N):
    S.add(str(input()))

for i in range(M):
    string = str(input())

    if string in S:
        cnt += 1
print(cnt)