import sys

M, N = [int(x) for x in sys.stdin.readline().split()]

def prime(A : int) :
    if A < 2 :
        return False
    for i in range(2, int(A**0.5) + 1) :
        if A%i == 0 :
            return False
    return True

for i in range(M, N+1) :
    if prime(i) :
        print(i)