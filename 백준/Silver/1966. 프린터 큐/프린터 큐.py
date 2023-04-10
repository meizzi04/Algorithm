import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    cnt = 0

    while queue:
        M -= 1

        if queue[0] == max(queue):
            queue.popleft()
            cnt += 1
            if M < 0:
                print(cnt)
                break
        else:
            queue.append(queue[0])
            queue.popleft()
            if M < 0:
                M = len(queue) - 1