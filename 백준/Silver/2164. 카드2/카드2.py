import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
card = deque(range(1, N+1))

while len(card) > 1:
    card.popleft()
    tmp = card.popleft()
    card.append(tmp)

print(*card)