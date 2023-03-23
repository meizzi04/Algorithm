import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
num = deque()

for i in range(1, N+1):
    num.append(i)

print('<', end='')

for i in range(N):
    for j in range(K-1):
        num.append(num.popleft())
    print(num.popleft(), end='')
    if i != N-1:
        print(',', end=' ')
print('>')