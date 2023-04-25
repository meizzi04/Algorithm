A, B = map(int, input().split())
C, D = map(int, input().split())

numerator = A*D + C*B
denominator = B*D

def gcd(x, y):
    mod = x % y

    while mod > 0:
        x = y
        y = mod
        mod = x % y
    return y

N = gcd(numerator, denominator)

print(numerator//N, denominator//N)