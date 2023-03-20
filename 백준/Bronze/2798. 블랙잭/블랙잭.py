import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
card = list(map(int, input().split()))
card_list = combinations(card, 3)
result = []

for i in card_list:
    if sum(i) > M:
        continue
    else:
        result.append(sum(i))

print(max(result))