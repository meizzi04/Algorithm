import sys

input = sys.stdin.readline

def prime(A: int):
    if A < 2:
        return False
    for i in range(2, int(A**0.5) + 1):
        if A % i == 0:
            return False
    return True

n = int(input())

for i in range(n):
    num = int(input())

    while True:
        if prime(num):
            print(num)
            break
        else:
            num += 1