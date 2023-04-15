import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    num = int(input())
    zero, one = 1, 0

    for j in range(num):
        zero, one = one, zero+one

    print(zero, one)