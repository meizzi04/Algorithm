import sys
input = sys.stdin.readline

K, N = map(int, input().split())
num = []
for i in range(K):
    num.append(int(input()))
start, end = 1, max(num)

while start <= end:
    mid = (start+end) // 2
    lan = 0

    for i in num:
        lan += i // mid

    if lan >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)