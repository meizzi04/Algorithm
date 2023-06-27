N = int(input())
dancer = {"ChongChong"}

for i in range(N):
    A, B = list(map(str, input().split()))

    if A in dancer:
        dancer.add(B)
    if B in dancer:
        dancer.add(A)

print(len(dancer))