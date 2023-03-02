N = int(input())
n = 1

while N >= n*(n+1)/2:
    n += 1

print(n-1)