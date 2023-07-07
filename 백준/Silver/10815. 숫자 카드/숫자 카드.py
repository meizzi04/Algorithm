import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))
M = int(input())
check_card = list(map(int, input().split()))

card.sort()

for i in check_card:
    left = bisect_left(card, i)
    right = bisect_right(card, i)
    print(right - left, end=" ")