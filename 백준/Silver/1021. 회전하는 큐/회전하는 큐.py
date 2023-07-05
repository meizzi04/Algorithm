from collections import deque

N, M = map(int, input().split())
num = list(map(int, input().split()))
dq = deque([i for i in range(1, N + 1)])

cnt = 0
for i in num:
    while True:
        if dq[0] == i:
            dq.popleft()
            break
        else:
            if dq.index(i) <= len(dq) // 2:
                dq.rotate(-1)
                cnt += 1
            else:
                dq.rotate(1)
                cnt += 1
print(cnt)