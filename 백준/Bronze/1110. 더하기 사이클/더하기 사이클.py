import sys

input = sys.stdin.readline

N = int(input())
tmp = N
cnt = 0

while True:
    sum = N // 10 + N % 10
    num = N % 10 * 10 + sum % 10
    cnt += 1
    N = num

    if num == tmp:
        break

print(cnt)