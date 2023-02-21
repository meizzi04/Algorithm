from itertools import permutations

N = int(input())
arr = list(map(int, input().split()))

arr_ = permutations(arr, N)
max_ = 0

for i in arr_ :
    tmp = 0

    for j in range(N-1) :
        tmp += abs(i[j] - i[j-1])

    max_ = max(max_, tmp)

print(max_)