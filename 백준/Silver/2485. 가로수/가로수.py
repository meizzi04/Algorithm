import sys
input = sys.stdin.readline

def gcd(A: int, B: int):
    if B == 0:
        return A
    else:
        return gcd(B, A % B)

N = int(input())
A = int(input())

tree = []

for i in range(N - 1):
    B = int(input())
    tree.append(B - A)
    A = B

g = tree[0]

for i in range(len(tree)):
    g = gcd(g, tree[i])

cnt = 0
for i in tree:
    cnt += i // g - 1
print(cnt)