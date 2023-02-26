import sys

input = sys.stdin.readline

N = int(input())
A = set(map(int, input().split()))
M = int(input())
M_num = list(map(int, input().split()))

for i in M_num:
    if i in A:
        print(1)
    else:
        print(0)