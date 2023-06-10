import sys

input = sys.stdin.readline

N = int(input())
x_ = []
y_ = []

for _ in range(N):
    x, y = map(int, input().split())
    x_.append(x)
    y_.append(y)

print((max(x_) - min(x_)) * (max(y_) - min(y_)))