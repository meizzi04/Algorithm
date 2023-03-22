import sys
input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))

M = int(input())
num = list(map(int, input().split()))

hash = {}

for i in card:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

for i in num:
    if i in hash:
        print(hash[i], end=' ')
    else:
        print(0, end=' ')